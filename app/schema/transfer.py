from pydantic import BaseModel


class Transfer(BaseModel):
    from_account_no: int
    to_account_no: int
    amount: float
