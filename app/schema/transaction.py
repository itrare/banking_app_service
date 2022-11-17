from enum import Enum
from pydantic import BaseModel


class TransactionType(str, Enum):
    Widthdraw = "transaction.widthdraw"
    Deposit = "transaction.deposit"


class Transaction(BaseModel):
    amount: float
    account_no: int
    type: TransactionType
