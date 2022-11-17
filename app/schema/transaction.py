from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TransactionType(str, Enum):
    Withdraw = "transaction.withdraw"
    Deposit = "transaction.deposit"
    Transfer = "transaction.transfer"


class Transaction(BaseModel):
    type: TransactionType
    credit_to: Optional[int]
    debit_from: Optional[int]
    amount: float
    account_no: int
    type: TransactionType
