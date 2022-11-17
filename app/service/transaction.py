from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction, TransactionType
from app.service.account import AccountService
from app.service.deposit import DepositService
from app.service.withdraw import WithdrawService


class TransactionService:

    def __init__(self, account_repo: AccountRepository, transaction_repo: TransactionRepository):
        self.account_service = AccountService(account_repo)
        self.deposit_service = DepositService(self.account_service, transaction_repo)
        self.withdraw_service = WithdrawService(self.account_service, transaction_repo)

    async def transaction(self, transaction: Transaction):
        output = None
        if transaction.type == TransactionType.Deposit:
            output = self.deposit_service.transaction(transaction)
        elif transaction.type == TransactionType.Widthdraw:
            output = self.withdraw_service.transaction(transaction)
        return output
