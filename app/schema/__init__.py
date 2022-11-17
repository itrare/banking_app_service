from enum import Enum


class QueryType(str, Enum):
    Create = "Create"
    Balance = "Balance"
    Deposit = "Deposit"
    Withdraw = "Withdraw"
    Transfer = "Transfer"
