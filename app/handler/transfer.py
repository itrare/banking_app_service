from app.handler import BaseExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction, TransactionType
from app.service.transfer import TransferService


class TransferExecutor(BaseExecutor):
    def __init__(
        self, account_repo: AccountRepository, transaction_repo: TransactionRepository
    ):
        self.transfer_service = TransferService(account_repo, transaction_repo)

    async def transfer(self, arguments):

        req = Transaction(
            type=TransactionType.Transfer,
            account_no=arguments[0],
            debit_from=arguments[0],
            credit_to=arguments[1],
            amount=arguments[2],
        )
        response = await self.transfer_service.transfer(req)
        return response
