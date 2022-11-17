from pydantic import BaseModel


class AccountCreateRequest(BaseModel):
    name: str


class AccountBalanceRequest(BaseModel):
    account_no: int
