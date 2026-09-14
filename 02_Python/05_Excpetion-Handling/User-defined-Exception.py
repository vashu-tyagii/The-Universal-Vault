"""User-defined exceptions in Python.

Notes
-----
* Create a custom exception by inheriting from ``Exception`` (or one of its
  subclasses).
* Use custom exceptions to describe application-specific errors clearly.
* ``raise`` signals an error; ``try``/``except`` handles it.
* Add useful context to the exception message and catch specific exceptions
  before broader ones.
"""


class InsufficientBalanceError(Exception):
    """Raised when an account does not have enough money for a withdrawal."""


class BankAccount:
    """A small example showing how to raise a user-defined exception."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # `self` refers to the current instance of BankAccount.
        # It stores the object's state (attributes) for this specific object.
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Cannot withdraw ${amount:.2f}; "
                f"available balance is ${self.balance:.2f}"
            )
        self.balance -= amount


def main() -> None:
    account = BankAccount("Ava", 100.00)

    try:
        account.withdraw(150.00)
    except InsufficientBalanceError as error:
        print(f"Withdrawal failed: {error}")
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print(f"Withdrawal successful. Balance: ${account.balance:.2f}")
    finally:
        print(f"Final balance: ${account.balance:.2f}")


if __name__ == "__main__":
    main()
