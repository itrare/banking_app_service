import pytest_asyncio

from app.handler import Handler
from app.handler.account import AccountExecutor
from app.handler.transaction import TransactionExecutor
from app.handler.transfer import TransferExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema import QueryType


@pytest_asyncio.fixture
async def handler():
    hndl = Handler()
    account_repo = AccountRepository(None)
    transaction_repo = TransactionRepository(None)

    # create query executor to handle specific task
    account_executor = AccountExecutor(account_repo)
    transaction_executor = TransactionExecutor(account_repo, transaction_repo)
    transfer_executor = TransferExecutor(account_repo, transaction_repo)

    # set executor for given set of queries
    _ = await hndl.set_executor(QueryType.Create, account_executor)
    _ = await hndl.set_executor(QueryType.Balance, account_executor)
    _ = await hndl.set_executor(QueryType.Deposit, transaction_executor)
    _ = await hndl.set_executor(QueryType.Withdraw, transaction_executor)
    _ = await hndl.set_executor(QueryType.Transfer, transfer_executor)

    return hndl
