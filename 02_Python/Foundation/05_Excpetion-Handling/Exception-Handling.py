"""Python Exception Handling

Exceptions are runtime errors that interrupt the normal flow of a program.
Handle expected errors so the program can respond gracefully instead of
crashing.

Main keywords
-------------
try     Code that may raise an exception.
except  Code that handles a matching exception.
else   Runs only when no exception occurs.
finally Runs whether an exception occurs or not (useful for cleanup).
raise   Creates an exception intentionally.

Good practice
-------------
* Catch specific exceptions, not a bare ``except``.
* Keep the try block small.
* Use ``as error`` when the error message is useful.
* Do not hide errors silently; report or log them.
"""


def divide_numbers(first_number: float, second_number: float) -> float | None:
	"""Divide two numbers while handling common input errors."""
	try:
		result = first_number / second_number
	except ZeroDivisionError:
		print("Error: a number cannot be divided by zero.")
		return None
	else:
		print(f"Result: {result}")
		return result


def read_integer(value: str) -> int | None:
	"""Convert text to an integer and handle invalid input."""
	try:
		number = int(value)
	except ValueError as error:
		print(f"Invalid integer: {error}")
		return None
	else:
		return number
	finally:
		# This block always runs, even when conversion fails.
		print("Conversion attempt finished.")


def require_positive(number: int) -> int:
	"""Raise an exception when a value does not meet a requirement."""
	if number <= 0:
		raise ValueError("number must be positive")
	return number


if __name__ == "__main__":
	divide_numbers(10, 2)
	divide_numbers(10, 0)

	print(read_integer("42"))
	print(read_integer("not a number"))

	try:
		require_positive(-3)
	except ValueError as error:
		print(f"Validation error: {error}")
