from aiosqlite import Connection


class AccountRepository:
    def __init__(self, connection: Connection):
        self.conn = connection

    async def create_account(self, account_holder_name: str):
        query = "INSERT INTO account(name, balance) VALUES (?, 0) RETURNING account_no"
        cur = await self.conn.execute(query, (account_holder_name,))
        result = await cur.fetchone()
        return result[0]

    async def fetch_balance(self, account_no: int):
        query = "SELECT balance FROM account WHERE account_no = ?"
        cur = await self.conn.execute(query, (account_no,))
        result = await cur.fetchone()
        return result[0]

    async def account_exists(self, account_no: int):
        query = "SELECT 1 FROM account WHERE account_no = $1"
        cur = await self.conn.execute(query, (account_no,))
        result = await cur.fetchone()
        return len(result) != 0
