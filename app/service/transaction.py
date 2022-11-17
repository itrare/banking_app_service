from app.schema.transaction import Transaction, TransactionType
from app.service.deposit import DepositService
from app.service.withdraw import WithdrawService


class TransactionService:
    def __init__(self):
        pass

    @staticmethod
    async def transaction(transaction: Transaction):
        if transaction.type == TransactionType.Deposit:
            output = DepositService.transaction(transaction)
        elif transaction.type == TransactionType.Widthdraw:
            output = WithdrawService.transaction(transaction)
        return output
