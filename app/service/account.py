from app.exceptions.exc import InvalidAccount
from app.repository.account import AccountRepository
from app.schema.account import AccountBalanceRequest, AccountCreateRequest


class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    async def create_account(self, request: AccountCreateRequest):
        account_no = await self.account_repo.create_account(
            account_holder_name=request.name
        )
        return account_no

    async def fetch_balance(self, request: AccountBalanceRequest):
        balance = await self.account_repo.fetch_balance(account_no=request.account_no)

        if balance is None:
            raise InvalidAccount

        return balance

    async def is_account_valid(self, account_no: int):
        ok = await self.account_repo.account_exists(account_no)
        return ok
