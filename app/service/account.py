from app.exceptions.exc import InvalidAccount
from app.repository.account import AccountRepository


class AccountService:

    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    async def create_account(self, account_request):
        new_account_details = await self.account_repo.create_account(account_request)
        return new_account_details["account_no"]

    async def fetch_balance(self, account_no):
        account_details = await self.account_repo.get_account_details(account_no)

        if not account_details:
            raise InvalidAccount

        return account_details["balance"]


