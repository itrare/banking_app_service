import asyncio

from app.exceptions.exc import BankingException


async def start_banking_service():
    try:
        pass
    except BankingException as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    loop = asyncio.get_running_loop()
    loop.run_until_complete(start_banking_service())
