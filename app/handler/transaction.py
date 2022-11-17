from app.handler import BaseExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction, TransactionType
from app.service.transaction import TransactionService


class TransactionExecutor(BaseExecutor):
    def __init__(
        self, account_repo: AccountRepository, transaction_repo: TransactionRepository
    ):
        self.transaction_service = TransactionService(account_repo, transaction_repo)

    async def deposit(self, arguments):
        # prepare request
        req = Transaction(
            type=TransactionType.Deposit,
            account_no=arguments[0],
            credit_to=arguments[0],
            amount=arguments[1],
        )
        response = await self.transaction_service.transaction(req)

        return response

    async def withdraw(self, arguments):
        # prepare request
        req = Transaction(
            type=TransactionType.Withdraw,
            account_no=arguments[0],
            debit_from=arguments[0],
            amount=arguments[1],
        )
        response = await self.transaction_service.transaction(req)
        return response
