from app.handler import BaseExecutor
from app.repository.account import AccountRepository
from app.schema.account import AccountBalanceRequest, AccountCreateRequest
from app.service.account import AccountService


class AccountExecutor(BaseExecutor):
    def __init__(self, account_repo: AccountRepository):
        self.account_service = AccountService(account_repo)

    async def create(self, arguments):
        # prepare request
        req = AccountCreateRequest(name=" ".join(arguments[0]))
        response = await self.account_service.create_account(req)

        return response

    async def balance(self, arguments):
        # prepare request
        req = AccountBalanceRequest(account_no=arguments[0])
        response = await self.account_service.fetch_balance(req)

        return response
