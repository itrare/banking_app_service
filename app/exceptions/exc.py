class BankingException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class MinimumDepositAmount(BankingException):
    """ Raises when the deposit amount have not met the criteria """

    def __init__(self):
        super().__init__("")


class MaximumDepositAmount(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class MinimumWithdrawAmount(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class MaximumWithdrawAmount(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class DepositLimitExhausted(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class WithdrawLimitExhausted(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class InvalidAccountNo(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class InsufficientBalance(BankingException):
    """"""

    def __init__(self):
        super().__init__("")


class BalanceLimitExceeds(BankingException):
    """"""

    def __init__(self):
        super().__init__("")
