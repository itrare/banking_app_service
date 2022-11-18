import pytest

from app.schema import QueryType


@pytest.mark.asyncio
@pytest.mark.usefixtures("handler")
class TestAccountExecutor:
    @pytest.mark.parametrize(
        "test_input, expected, patches",
        [
            (
                "Abhishek",
                1001,
                [
                    ("app.repository.account.AccountRepository.create_account", 1001),
                ],
            ),
            (
                "John",
                1002,
                [
                    ("app.repository.account.AccountRepository.create_account", 1002),
                ],
            ),
        ],
    )
    async def test_create_dynamic(self, mocker, handler, test_input, expected, patches):
        for ptch in patches:
            mocker.patch(
                ptch[0],
                return_value=ptch[1],
            )
        try:
            output = await handler.run_executor(QueryType.Create, test_input.split(" "))
            assert output == expected
        except Exception as e:
            assert e.__str__() == expected

    @pytest.mark.parametrize(
        "test_input, expected, patches",
        [
            (
                "10011",
                "Account does not exist",
                [
                    ("app.repository.account.AccountRepository.fetch_balance", None),
                ],
            ),
        ],
    )
    async def test_balance_dynamic(
        self, mocker, handler, test_input, expected, patches
    ):
        for ptch in patches:
            mocker.patch(
                ptch[0],
                return_value=ptch[1],
            )
        try:
            output = await handler.run_executor(
                QueryType.Balance, test_input.split(" ")
            )
            assert output == expected
        except Exception as e:
            assert e.__str__() == expected
