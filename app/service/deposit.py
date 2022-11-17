from app.core.config import MAXIMUM_DEPOSIT_AMOUNT, MINIMUM_DEPOSIT_AMOUNT
from app.exceptions.exc import MaximumDepositAmount, MinimumDepositAmount
from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction
from app.service.account import AccountService


class DepositService:

    def __init__(self, account_service: AccountService, transaction_repo: TransactionRepository):
        self.transaction_repo = transaction_repo
        self.account_service = account_service

    async def transaction(self, transaction: Transaction):
        if await self.validate_deposit(transaction):
            pass

    async def validate_deposit(self, transaction):
        # check if the account has amount greater or equals to withdraw amount

        if transaction.amount > MAXIMUM_DEPOSIT_AMOUNT:
            raise MaximumDepositAmount

        if transaction.amount < MINIMUM_DEPOSIT_AMOUNT:
            raise MinimumDepositAmount

        return True
