# Curve Notebooks

Notebooks are easy-to-use tools written in Python, designed to showcase the usage of smart contracts and their functionalities. They can be interactively designed and run directly in the browser to make the user experience as easy and smooth as possible. They encompass:

- Smart Contract Navigation: Showcasing smart contract functionalities.
- Data Analysis and Research.
- Integration guidelines for functionalities such as oracles, etc.

**For a list of all hosted notebooks, see here:** https://docs.curve.fi/references/notebooks/

---

## Running Notebooks

For notebooks hosted on Google Colab, a user only needs to [set up two "Secrets"](https://medium.com/@parthdasawant/how-to-use-secrets-in-google-colab-450c38e3ec75). For consistency, all notebooks use a secret named `RPC_ETHEREUM` for HTTP API keys (e.g., from [Alchemy](https://www.alchemy.com/)) and an `ETHERSCAN_API_KEY` secret holding a valid [Etherscan API key](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics).

After setting up these two secrets, the notebook can be successfully run directly in the browser.

## Hosting

The first notebooks were hosted on a [JupyterHub server from Vyper](https://try.vyperlang.org/hub/). Due to performance issues, hosting was switched to [Google Colab](https://colab.google/). Old notebooks remain hosted on the JupyterHub server, but all new ones will be hosted on Google Colab.

## Vyper and Titanoboa

All Curve Smart Contracts are written in [Vyper](https://github.com/vyperlang).

For notebooks, mostly ["Titanoboa"](https://github.com/vyperlang/titanoboa) is used. Titanoboa is a Vyper interpreter with pretty tracebacks, forking, debugging features, and more! Titanoboa's goal is to provide a modern, advanced, and integrated development experience for Vyper users.

## Running Locally 

The notebooks in this repository are not designed to be run locally. This is just the copy-pasted source code of the hosted notebooks. When trying to run these locally, there need to be some tweaks, especially with regard to the API keys.

## Contributing

Everyone is very welcome to contribute any kind of notebooks to the repo. Feel free to just create a PR.