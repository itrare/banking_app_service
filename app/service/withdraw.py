from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction
from app.service.account import AccountService


class WithdrawService:
    def __init__(self, account_service: AccountService, transaction_repo: TransactionRepository):
        self.transaction_repo = transaction_repo
        self.account_service = account_service

    async def transaction(self, transaction: Transaction):
        pass

    @staticmethod
    async def validate_withdraw(self, transaction: Transaction):
        # check if the account has amount greater or equals to withdraw amount
        balance = self.account_service.fetch_balance(transaction.account_no)

        if
