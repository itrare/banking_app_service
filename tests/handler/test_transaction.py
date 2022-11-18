import pytest

from app.schema import QueryType


@pytest.mark.asyncio
@pytest.mark.usefixtures("handler")
class TestTransactionExecutor:
    @pytest.mark.parametrize(
        "test_input, expected, patches",
        [
            (
                "1001 500",
                500,
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                    ("app.repository.transaction.TransactionRepository.deposit", 500),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 0)
                ],
            ),
            (
                "1001 1000",
                1500,
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 500),
                    ("app.repository.transaction.TransactionRepository.deposit", 1500),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 1)
                ],
            ),
            (
                "1001 100",
                "Minimum deposit amount is 500",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 500),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 1)
                ],
            ),
            (
                "1001 60000",
                'Maximum deposit amount is 50000',
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 1)
                ],
            ),
            (
                "1001 10000",
                11500,
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 1500),
                    ("app.repository.transaction.TransactionRepository.deposit", 11500),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 2)
                ],
            ),
            (
                "1001 10000",
                "Only 3 deposits are allowed in a day",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 11500),
                    ("app.repository.account.AccountRepository.fetch_balance", 11500),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 3)
                ],
            ),
        ],
    )
    async def test_deposit_dynamic(
        self, mocker, handler, test_input, expected, patches
    ):
        for ptch in patches:
            mocker.patch(
                ptch[0],
                return_value=ptch[1],
            )
        try:
            output = await handler.run_executor(
                QueryType.Deposit, test_input.split(" ")
            )
            assert output == expected
        except Exception as e:
            print(expected)
            assert e.__str__() == expected

    @pytest.mark.parametrize(
        "test_input, expected, patches",
        [
            (
                "1001 500",
                "Minimum withdrawal amount is 1000",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 0),
                    ("app.repository.transaction.TransactionRepository.withdraw", 11500),
                ],
            ),
            (
                "1001 20000",
                "Insufficient balance",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                    ("app.repository.transaction.TransactionRepository.withdraw", 0),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 0),
                ],
            ),
            (
                "1001 1000",
                10500,
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 11500),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 0),
                    ("app.repository.transaction.TransactionRepository.withdraw", 10500),
                ],
            ),
            (
                "1001 1900",
                8600,
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 10500),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 1),
                    ("app.repository.transaction.TransactionRepository.withdraw", 8600),
                ],
            ),
            (
                "1001 1000",
                7600,
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 8600),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 2),
                    ("app.repository.transaction.TransactionRepository.withdraw", 7600),
                ],
            ),
            (
                "1001 5000",
                "Only 3 withdrawals are allowed in a day",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 7600),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 3),
                ],
            ),
        ],
    )
    async def test_withdraw_dynamic(
        self, mocker, handler, test_input, expected, patches
    ):
        for ptch in patches:
            mocker.patch(
                ptch[0],
                return_value=ptch[1],
            )
        try:
            output = await handler.run_executor(
                QueryType.Withdraw, test_input.split(" ")
            )
            assert output == expected
        except Exception as e:
            assert e.__str__() == expected
