from pydantic import BaseModel


class Account(BaseModel):
    customer_name: str
    account_id: int
    balance: float

