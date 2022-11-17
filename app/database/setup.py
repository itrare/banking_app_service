from aiosqlite import Connection

from app.database.migrations.V0001_accounts import migrate as V0001


async def setup_db(conn: Connection):

    await V0001(conn)
