from app.core.config import MAXIMUM_WITHDRAW_AMOUNT, MINIMUM_WITHDRAW_AMOUNT
from app.exceptions.exc import InsufficientBalance, MaximumWithdrawAmount, MinimumWithdrawAmount
from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction
from app.service.account import AccountService


class WithdrawService:
    def __init__(self, account_service: AccountService, transaction_repo: TransactionRepository):
        self.transaction_repo = transaction_repo
        self.account_service = account_service

    async def transaction(self, transaction: Transaction):
        if await self.validate_withdraw(transaction):
            pass

    async def validate_withdraw(self, transaction: Transaction):
        # check if the account has amount greater or equals to withdraw amount
        balance = await self.account_service.fetch_balance(transaction.account_no)

        if balance < transaction.amount:
            raise InsufficientBalance
        
        if transaction.amount > MAXIMUM_WITHDRAW_AMOUNT:
            raise MaximumWithdrawAmount

        if transaction.amount < MINIMUM_WITHDRAW_AMOUNT:
            raise MinimumWithdrawAmount

        return True



