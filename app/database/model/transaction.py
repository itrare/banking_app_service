from pydantic import BaseModel


class Transaction(BaseModel):
    transaction_id: int
    transaction_type: str
    debit_from: int
    credit_to: int
    amount: float
