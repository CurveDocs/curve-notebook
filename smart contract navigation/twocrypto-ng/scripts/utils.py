import boa
import pandas as pd

def deploy_infra():
    """
    Function to deploy the twocrypto-ng infrastructure.
    The following contracts are deployed:
    - two mock coins (coin_a, coin_b)
    - Factory
    - Pool implementation
    - Gauge implementation
    - Math implementation
    - Views implementation

    Admin and fee_receiver is set to a randomly generated address.
    """
    # Generate addresses
    admin = boa.env.generate_address()
    fee_receiver = boa.env.generate_address()
    trader = boa.env.generate_address()
    
    # Load mock coins
    coin_a = boa.load("../contracts/mocks/ERC20Mock.vy", "coin_a", "coin_a", 18)
    coin_b = boa.load("../contracts/mocks/ERC20Mock.vy", "coin_b", "coin_b", 18)

    # Mint coins for trader
    coin_a._mint_for_testing(trader, 10**23, sender=trader)
    coin_b._mint_for_testing(trader, 10**23, sender=trader)

    # Load contract implementations
    pool_implementation = boa.load_partial("../contracts/main/CurveTwocryptoOptimized.vy")
    gauge_implementation = boa.load_partial("../contracts/main/LiquidityGauge.vy")
    math_implementation = boa.load("../contracts/main/CurveCryptoMathOptimized2.vy")
    views_implementation = boa.load("../contracts/main/CurveCryptoViews2Optimized.vy")

    # Initialize factory contract
    with boa.env.prank(admin):
        factory = boa.load("../contracts/main/CurveTwocryptoFactory.vy")
        factory.initialise_ownership(fee_receiver, admin)
        factory.set_pool_implementation(pool_implementation.deploy_as_blueprint().address, 0)
        factory.set_gauge_implementation(gauge_implementation.deploy_as_blueprint().address)
        factory.set_math_implementation(math_implementation.address)
        factory.set_views_implementation(views_implementation.address)

    # Return all relevant information
    return {
        "admin": admin,
        "fee_receiver": fee_receiver,
        "trader": trader,
        "coin_a": coin_a,
        "coin_b": coin_b,
        "factory": factory,
        "impl": pool_implementation,
        "pool_implementation": factory.pool_implementations(0),
        "gauge_implementation": factory.gauge_implementation(),
        "math_implementation": factory.math_implementation(),
        "views_implementation": factory.views_implementation()
    }



def deploy_pool(factory, coin_a, coin_b):
    """
    Function to deploy a pool based on the parameters below.
    Args:
    - factory (address)
    - coin_a (address)
    - coin_b (address)
    """

    name = "test"
    symbol = "test"
    coins = [coin_a.address, coin_b.address]
    implementation_id = 0
    A = 400000
    gamma = 145000000000000
    mid_fee = 26000000
    out_fee = 45000000
    allowed_extra_profit = 2000000000000
    fee_gamma = 230000000000000
    adjustment_step = 146000000000000
    ma_time = 600
    xcp_ma_time = 1800 * 24
    initial_price = 10**18  # 1:1 at the start
    admin_fee = 5 * 10**9


    # deploying the pool

    pool = factory.deploy_pool(
        name, symbol, coins,
        implementation_id, A, gamma, mid_fee, out_fee, fee_gamma, allowed_extra_profit, adjustment_step, int(ma_time/0.693), initial_price
    )
    return pool



def get_balances(trader, pool, coin_a, coin_b):
    # Assuming coin_a, coin_b, and pool are defined elsewhere in your code
    trader_balance_a = coin_a.balanceOf(trader)
    trader_balance_b = coin_b.balanceOf(trader)
    lp_tokens = pool.balanceOf(trader)
    pool_balance_a = pool.balances(0)
    pool_balance_b = pool.balances(1)

    # Create a DataFrame for balances
    data = {
        "Asset": ["Trader: Balance A", "Trader: Balance B", "Trader: LP Tokens", "Pool: Balance A", "Pool: Balance B"],
        "Balance": [
            trader_balance_a / 10**18,
            trader_balance_b / 10**18,
            lp_tokens / 10**18,
            pool_balance_a / 10**18,
            pool_balance_b / 10**18
        ]
    }

    return pd.DataFrame(data)