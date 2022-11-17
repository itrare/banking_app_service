from app.handler import BaseExecutor
from app.repository.account import AccountRepository
from app.service.account import AccountService


class AccountExecutor(BaseExecutor):

    def __init__(self, account_repo: AccountRepository):
        self.account_service = AccountService(account_repo)

    async def account_create(self):
        # prepare request
        req = None
        response = await self.account_service.create_account(req)

        return response

    async def account_balance(self):
        # prepare request
        req = None
        response =  self.account_service.fetch_balance(req)

        return response


