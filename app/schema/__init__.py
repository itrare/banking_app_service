from enum import Enum


class QueryType(str, Enum):
    Create = "account_create"
    Balance = "account_balance"
    Deposit = "deposit"
    Withdraw = "withdraw"
    Transfer = "transfer"
