# @version 0.3.10

admin: public(address)
future_admin: public(address)


event TransferOwnership:
    _old_owner: address
    _new_owner: address

@external
def __init__(_admin: address):
    self.admin = _admin


@external
def commit_transfer_ownership(_addr: address):
    """
    @notice Transfer ownership of this contract to `addr`
    @param _addr Address of the new owner
    """
    assert msg.sender == self.admin, "dev: admin only"

    self.future_admin = _addr


@external
def accept_transfer_ownership():
    """
    @notice Accept a pending ownership transfer
    @dev Only callable by the new owner
    """
    assert msg.sender == self.future_admin, "dev: future admin only"

    log TransferOwnership(self.admin, msg.sender)
    self.admin = msg.sender