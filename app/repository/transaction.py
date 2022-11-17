from aiosqlite import Connection

from app.schema.transaction import Transaction

query_cr_debit = "UPDATE account SET balance = ? WHERE account_no = ?"
query_add_transaction = """INSERT INTO "transaction" (account_no, credited_to, debited_from, amount, transacted_at, type) 
                            VALUES (?, ?, ?, ?, date('now'), ?) RETURNING transaction_id"""


class TransactionRepository:
    def __init__(self, connection: Connection):
        self.conn = connection

    async def fetch_balance(self, account_no: int):
        query = "SELECT balance FROM account WHERE account_no = ?"
        cur = await self.conn.execute(query, (account_no,))
        result = await cur.fetchone()
        return result[0]

    async def transfer(self, transaction_request: Transaction):

        balance_for_debit = await self.fetch_balance(transaction_request.debit_from)
        balance_for_credit = await self.fetch_balance(transaction_request.credit_to)
        await self.conn.execute(
            query_cr_debit,
            (
                balance_for_debit - transaction_request.amount,
                transaction_request.debit_from,
            ),
        )
        await self.conn.execute(
            query_cr_debit,
            (
                balance_for_credit + transaction_request.amount,
                transaction_request.credit_to,
            ),
        )

        result = await self.conn.execute(
            query_add_transaction,
            (
                transaction_request.credit_to,
                transaction_request.debit_from,
                transaction_request.amount,
                transaction_request.type,
            ),
        )
        _ = await self.conn.execute(
            query_add_transaction,
            (
                transaction_request.credit_to,
                transaction_request.debit_from,
                transaction_request.amount,
                transaction_request.type,
            ),
        )

        row = await result.fetchone()
        return row[0]

    async def deposit(self, transaction_request: Transaction):
        balance = await self.fetch_balance(transaction_request.account_no)
        await self.conn.execute(
            query_cr_debit,
            (balance + transaction_request.amount, transaction_request.credit_to),
        )
        _ = await self.conn.execute(
            query_add_transaction,
            (
                transaction_request.account_no,
                transaction_request.credit_to,
                transaction_request.debit_from,
                transaction_request.amount,
                transaction_request.type,
            ),
        )
        balance = await self.fetch_balance(transaction_request.account_no)
        return balance

    async def withdraw(self, transaction_request: Transaction):
        balance = await self.fetch_balance(transaction_request.account_no)
        await self.conn.execute(
            query_cr_debit,
            (balance - transaction_request.amount, transaction_request.debit_from),
        )
        _ = await self.conn.execute(
            query_add_transaction,
            (
                transaction_request.account_no,
                transaction_request.credit_to,
                transaction_request.debit_from,
                transaction_request.amount,
                transaction_request.type,
            ),
        )
        balance = await self.fetch_balance(transaction_request.account_no)
        return balance

    async def get_todays_deposits(self, account_no: int):
        query = """SELECT COUNT(transaction_id) FROM "transaction" WHERE account_no = ? and type = 
        'transaction.deposit' and transacted_at = date('now') """
        result = await self.conn.execute(query, (account_no,))
        row = await result.fetchone()
        if len(row):
            return row[0]
        return 0

    async def get_todays_withdraws(self, account_no: int):
        query = """SELECT COUNT(transaction_id) FROM "transaction" WHERE account_no = ? and type = 
        'transaction.withdraw' and transacted_at = date('now') """
        result = await self.conn.execute(query, (account_no,))
        row = await result.fetchone()

        if len(row):
            return row[0]
        return 0
