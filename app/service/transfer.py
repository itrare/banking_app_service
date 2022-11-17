from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.service.account import AccountService


class TransferService:
    def __init__(self, account_repo: AccountRepository, transaction_repo: TransactionRepository):
        self.account_service = AccountService(account_repo)
        self.transaction_repo = transaction_repo

    async def transfer(self, transfer_request):
        pass

    async def validate_transfer(self):
        pass
