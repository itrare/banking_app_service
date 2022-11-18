from app.core.config import (MAXIMUM_WITHDRAW_AMOUNT, MINIMUM_WITHDRAW_AMOUNT,
                             WITHDRAW_DAY_LIMIT)
from app.exceptions.exc import (InsufficientBalance, MaximumWithdrawAmount,
                                MinimumWithdrawAmount, WithdrawLimitExhausted)
from app.repository.transaction import TransactionRepository
from app.schema.account import AccountBalanceRequest
from app.schema.transaction import Transaction
from app.service.account import AccountService


class WithdrawService:
    def __init__(
        self, account_service: AccountService, transaction_repo: TransactionRepository
    ):
        self.transaction_repo = transaction_repo
        self.account_service = account_service

    async def transaction(self, transaction: Transaction):
        if await self.validate_withdraw(transaction):
            new_balance = await self.transaction_repo.withdraw(transaction)
            return new_balance

    async def validate_withdraw(self, transaction: Transaction):

        if transaction.amount > MAXIMUM_WITHDRAW_AMOUNT:
            raise MaximumWithdrawAmount

        if transaction.amount < MINIMUM_WITHDRAW_AMOUNT:
            raise MinimumWithdrawAmount

        no_of_withdraws_today = await self.transaction_repo.get_todays_withdraws(
            transaction.account_no
        )

        if no_of_withdraws_today == WITHDRAW_DAY_LIMIT:
            raise WithdrawLimitExhausted

        # check if the account has the amount greater or equals to withdraw amount
        balance = await self.account_service.fetch_balance(
            AccountBalanceRequest(account_no=transaction.account_no)
        )

        if balance < transaction.amount:
            raise InsufficientBalance

        return True
