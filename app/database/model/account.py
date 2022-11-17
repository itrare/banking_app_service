from pydantic import BaseModel


class Account(BaseModel):
    name: str
    account_id: int
    balance: float
