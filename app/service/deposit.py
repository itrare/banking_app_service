from app.core.config import (DEPOSIT_DAY_LIMIT, MAXIMUM_ACCOUNT_BALANCE_LIMIT,
                             MAXIMUM_DEPOSIT_AMOUNT, MINIMUM_DEPOSIT_AMOUNT)
from app.exceptions.exc import (BalanceLimitExceeds, DepositLimitExhausted,
                                MaximumDepositAmount, MinimumDepositAmount)
from app.repository.transaction import TransactionRepository
from app.schema.account import AccountBalanceRequest
from app.schema.transaction import Transaction
from app.service.account import AccountService


class DepositService:
    def __init__(
        self, account_service: AccountService, transaction_repo: TransactionRepository
    ):
        self.transaction_repo = transaction_repo
        self.account_service = account_service

    async def transaction(self, transaction: Transaction):
        if await self.validate_deposit(transaction):
            new_balance = await self.transaction_repo.deposit(transaction)
            return new_balance

    async def validate_deposit(self, transaction: Transaction):
        # check if the account has the amount less than balance limit.
        # check if the deposit is between minimum and maximum deposit amount.

        if transaction.amount > MAXIMUM_DEPOSIT_AMOUNT:
            raise MaximumDepositAmount

        if transaction.amount < MINIMUM_DEPOSIT_AMOUNT:
            raise MinimumDepositAmount

        balance = await self.account_service.fetch_balance(
            AccountBalanceRequest(account_no=transaction.account_no)
        )
        future_balance = balance + transaction.amount

        if future_balance > MAXIMUM_ACCOUNT_BALANCE_LIMIT:
            raise BalanceLimitExceeds

        no_of_deposits_today = await self.transaction_repo.get_todays_deposits(
            transaction.account_no
        )

        if no_of_deposits_today == DEPOSIT_DAY_LIMIT:
            raise DepositLimitExhausted

        return True
