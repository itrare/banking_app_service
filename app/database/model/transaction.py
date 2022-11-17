from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schema.transaction import TransactionType


class Transaction(BaseModel):
    transaction_id: int
    transaction_type: TransactionType
    debit_from: Optional[int]
    credit_to: Optional[int]
    amount: float
    created_at: datetime
