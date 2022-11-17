from pydantic import BaseModel


class AccountCreateRequest(BaseModel):
    name: str

