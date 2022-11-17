from app.core.config import (DEPOSIT_DAY_LIMIT, MAXIMUM_DEPOSIT_AMOUNT,
                             MAXIMUM_WITHDRAW_AMOUNT, MINIMUM_DEPOSIT_AMOUNT,
                             MINIMUM_WITHDRAW_AMOUNT, WITHDRAW_DAY_LIMIT)


class BankingException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class MinimumDepositAmount(BankingException):
    """Raises when the deposit amount have not met the criteria"""

    def __init__(self, message=f"Minimum deposit amount is {MINIMUM_DEPOSIT_AMOUNT}"):
        super().__init__(message)


class MaximumDepositAmount(BankingException):
    """"""

    def __init__(self, message=f"Maximum deposit amount is {MAXIMUM_DEPOSIT_AMOUNT}"):
        super().__init__(message)


class MinimumWithdrawAmount(BankingException):
    """"""

    def __init__(
        self, message=f"Minimum withdrawal amount is {MINIMUM_WITHDRAW_AMOUNT}"
    ):
        super().__init__(message)


class MaximumWithdrawAmount(BankingException):
    """"""

    def __init__(
        self, message=f"Maximum withdrawal amount is {MAXIMUM_WITHDRAW_AMOUNT}"
    ):
        super().__init__(message)


class DepositLimitExhausted(BankingException):
    """"""

    def __init__(
        self, message=f"Only {DEPOSIT_DAY_LIMIT} deposits are allowed in a day"
    ):
        super().__init__(message)


class WithdrawLimitExhausted(BankingException):
    """"""

    def __init__(
        self, message=f"Only {WITHDRAW_DAY_LIMIT} withdrawals are allowed in a day"
    ):
        super().__init__(message)


class InvalidAccount(BankingException):
    """"""

    def __init__(self, message="Account does not exist"):
        super().__init__(message)


class InsufficientBalance(BankingException):
    """"""

    def __init__(self, message="Insufficient balance"):
        super().__init__(message)


class BalanceLimitExceeds(BankingException):
    """"""

    def __init__(self, message="Balance Limit Exceeds"):
        super().__init__(message)
