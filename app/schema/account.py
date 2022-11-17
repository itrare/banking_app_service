from pydantic import BaseModel


class Customer(BaseModel):
    customer_id: int
    name: str


class Account(BaseModel):
    customer_id: int
    account_no: int
    balance: float
