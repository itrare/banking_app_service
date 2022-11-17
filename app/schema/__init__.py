from enum import Enum


class InvocationType(str, Enum):
    Create = "account.create"
    Deposit = "account.deposit"
    Withdraw = "account.withdraw"
    Balance = "account.balance"
    Transfer = "account.transfer"
