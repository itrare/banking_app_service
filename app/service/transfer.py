from app.core.config import MAXIMUM_WITHDRAW_AMOUNT, MINIMUM_WITHDRAW_AMOUNT
from app.exceptions.exc import (InvalidAccount, MaximumDepositAmount,
                                MaximumWithdrawAmount, MinimumDepositAmount,
                                MinimumWithdrawAmount, WithdrawLimitExhausted)
from app.repository.account import AccountRepository
from app.repository.transaction import TransactionRepository
from app.schema.transaction import Transaction, TransactionType
from app.service.account import AccountService
from app.service.deposit import DepositService
from app.service.withdraw import WithdrawService


class TransferService:
    def __init__(
        self, account_repo: AccountRepository, transaction_repo: TransactionRepository
    ):
        self.account_service = AccountService(account_repo)
        self.transaction_repo = transaction_repo
        self.withdraw_service = WithdrawService(self.account_service, transaction_repo)
        self.deposit_service = DepositService(self.account_service, transaction_repo)

    async def transfer(self, transfer_request: Transaction):
        ok = False
        if await self.validate_transfer(transfer_request):
            ok = await self.transaction_repo.transfer(transfer_request)

        if ok:
            return "Successful"

        return "Failure"

    async def validate_transfer(self, transfer_request: Transaction):

        try:
            valid_withdraw = await self.withdraw_service.validate_withdraw(
                Transaction(
                    account_no=transfer_request.debit_from,
                    type=TransactionType.Withdraw,
                    amount=transfer_request.amount,
                )
            )

        except MaximumWithdrawAmount:
            raise WithdrawLimitExhausted(
                f"Maximum withdrawal amount is {MAXIMUM_WITHDRAW_AMOUNT} for account {transfer_request.debit_from}"
            )

        except MinimumWithdrawAmount:
            raise WithdrawLimitExhausted(
                f"Minimum withdrawal amount is {MINIMUM_WITHDRAW_AMOUNT} for account {transfer_request.debit_from}"
            )

        except Exception:
            valid_withdraw = True

        try:
            valid_deposit = await self.deposit_service.validate_deposit(
                Transaction(
                    account_no=transfer_request.credit_to,
                    type=TransactionType.Deposit,
                    amount=transfer_request.amount,
                )
            )

        except MaximumDepositAmount:
            raise WithdrawLimitExhausted(
                f"Maximum withdrawal amount is {MAXIMUM_WITHDRAW_AMOUNT} for account f{transfer_request.credit_to}"
            )

        except MinimumDepositAmount:
            raise WithdrawLimitExhausted(
                f"Minimum withdrawal amount is {MINIMUM_WITHDRAW_AMOUNT} for account f{transfer_request.credit_to}"
            )

        except Exception:
            valid_deposit = True

        if not await self.account_service.is_account_valid(transfer_request.credit_to):
            raise InvalidAccount("destination account is invalid")

        if not await self.account_service.is_account_valid(transfer_request.debit_from):
            raise InvalidAccount

        return valid_deposit and valid_withdraw
