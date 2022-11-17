import asyncio

from app.exceptions.exc import BankingException
from app.handler import Handler
from app.handler.account import AccountExecutor
from app.handler.transaction import TransactionExecutor
from app.handler.transfer import TransferExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema import QueryType


async def start_banking_service():
    try:
        handler = Handler()

        # initialize database repositories
        account_repo = AccountRepository()
        transaction_repo = TransactionRepository()

        # create query executor to handle specific task
        account_executor = AccountExecutor(account_repo)
        transaction_executor = TransactionExecutor(account_repo, transaction_repo)
        transfer_executor = TransferExecutor(account_repo, transaction_repo)

        # set executor for given set of queries
        _ = await handler.set_executor(QueryType.Create, account_executor)
        _ = await handler.set_executor(QueryType.Balance, account_executor)
        _ = await handler.set_executor(QueryType.Deposit, transaction_executor)
        _ = await handler.set_executor(QueryType.Withdraw, transaction_executor)
        _ = await handler.set_executor(QueryType.Transfer, transfer_executor)

        while True:
            try:
                _ = await handler.run()

            except KeyboardInterrupt:
                break

    except BankingException as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    loop = asyncio.get_running_loop()
    loop.run_until_complete(start_banking_service())
