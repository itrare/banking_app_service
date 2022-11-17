from pydantic import BaseModel
from typing import Optional


class Account(BaseModel):
    account_holder_name: str
    account_id: int
    balance: float


class Transaction(BaseModel):
    transaction_id: int
    cr_dr_type: str
    debit_from: int
    credit_to: int
    amount: float
    remarks: Optional[str] = ""
