from app.handler import BaseExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.service.account import AccountService
from app.service.transfer import TransferService


class TransferExecutor(BaseExecutor):
    def __init__(self, account_repo: AccountRepository, transaction_repo: TransactionRepository):
        self.account_service = AccountService(account_repo)
        self.transaction_service = TransferService(account_repo, transaction_repo)


    async def transfer(self):
        pass
