import argparse
import asyncio
import aiosqlite

from app.core.config import INPUT_FILE_PATH
from app.database.setup import setup_db
from app.exceptions.exc import BankingException
from app.handler import Handler
from app.handler.account import AccountExecutor
from app.handler.transaction import TransactionExecutor
from app.handler.transfer import TransferExecutor
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema import QueryType


async def start_banking_service():
    parser = argparse.ArgumentParser(description="Banking App Cli")
    parser.add_argument("--initdb", type=bool, default=False)
    args = parser.parse_args()
    try:
        handler = Handler()

        # initialize database repositories
        con = await aiosqlite.connect("banking_app.db").__aenter__()

        if args.initdb:
            await setup_db(con)

        account_repo = AccountRepository(con)
        transaction_repo = TransactionRepository(con)

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
                await handler.run(input_filepath=INPUT_FILE_PATH)

            except KeyboardInterrupt:
                break

            except Exception as e:
                if e.__str__() == "listen_done":
                    break
        return
                # print(e)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_banking_service())
