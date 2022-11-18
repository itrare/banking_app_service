import pytest

from app.schema import QueryType


@pytest.mark.asyncio
@pytest.mark.usefixtures("handler")
class TestTransferExecutor:
    @pytest.mark.parametrize(
        "test_input, expected, patches",
        [
            (
                "1001 1002 5000",
                "Successful",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                    ("app.repository.account.AccountRepository.account_exists", True),
                    ("app.repository.transaction.TransactionRepository.transfer", 1001),
                    ("app.repository.transaction.TransactionRepository.get_todays_withdraws", 0),
                    ("app.repository.transaction.TransactionRepository.get_todays_deposits", 0),
                ],
            ),
            (
                "1002 1004 500",
                "Minimum withdrawal amount is 1000 for account 1002",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                ],
            ),
            (
                "1002 1004 30000",
                "Maximum withdrawal amount is 25000 for account 1002",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", 0),
                ],
            ),
        ],
    )
    async def test_transfer_dynamic(
        self, mocker, handler, test_input, expected, patches
    ):
        for ptch in patches:
            mocker.patch(
                ptch[0],
                return_value=ptch[1],
            )
        try:
            output = await handler.run_executor(
                QueryType.Transfer, test_input.split(" ")
            )
            assert output == expected
        except Exception as e:
            assert e.__str__() == expected
