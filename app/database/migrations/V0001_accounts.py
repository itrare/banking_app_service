from aiosqlite import Connection


async def migrate(conn: Connection):
    await conn.execute(
        """CREATE TABLE IF NOT EXISTS "account" (
            account_no INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            balance DECIMAL(10, 2) NOT NULL
        )"""
    )
    await conn.execute(
        """CREATE TABLE IF NOT EXISTS "transaction" (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_no INTEGER NOT NULL,
            credited_to INT,
            debited_from INT,
            amount DECIMAL(10, 2) NOT NULL,
            transacted_at TEXT,
            type VARCHAR(255) NOT NULL,
        
            CONSTRAINT transaction_account_cr_fk FOREIGN KEY (credited_to) REFERENCES account (account_no),
            CONSTRAINT transaction_account_dr_fk FOREIGN KEY (debited_from) REFERENCES account (account_no),
            CONSTRAINT transaction_account_self_fk FOREIGN KEY (account_no) REFERENCES account (account_no)
        )"""
    )
    await conn.execute(
        """UPDATE SQLITE_SEQUENCE SET seq = 1000 WHERE name = 'transaction'"""
    )
    await conn.execute(
        """UPDATE SQLITE_SEQUENCE SET seq = 1000 WHERE name = 'account'"""
    )
