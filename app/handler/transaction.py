from app.handler import BaseExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.service.account import AccountService
from app.service.transaction import TransactionService


class TransactionExecutor(BaseExecutor):
    def __init__(self, account_repo: AccountRepository, transaction_repo: TransactionRepository):
        self.account_service = AccountService(account_repo)
        self.transaction_service = TransactionService(account_repo, transaction_repo)

    async def deposit(self):
        # prepare request
        req = None
        response = await self.transaction_service.transaction(req)

        return response

    async def withdraw(self):
        # prepare request
        req = None
        response = await self.transaction_service.transaction(req)
        return response
