"""Recursion notes and examples.

Recursion is when a function calls itself to solve a smaller version of the
same problem. A correct recursive function has:

1. A base case that stops the calls.
2. A recursive case that moves toward the base case.

Recursive calls use Python's call stack. Very deep recursion can raise
RecursionError, so a loop is often better for large inputs.
"""


def factorial(n: int) -> int:
    """Return n! for a non-negative integer."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:  # Base case: 0! and 1! are both 1.
        return 1
    return n * factorial(n - 1)  # Recursive case.
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)

def sum_to(n: int) -> int:
    """Return 1 + 2 + ... + n using recursion."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:  # Base case.
        return 0
    return n + sum_to(n - 1)  # Smaller problem: sum_to(n - 1).


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (simple teaching example)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:  # Base cases: fib(0)=0 and fib(1)=1.
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def countdown(n: int) -> None:
    """Print n down to 1, then stop at the base case."""
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)


if __name__ == "__main__":
    print(factorial(5))  # 120
    print(sum_to(5))  # 15
    print(fibonacci(7))  # 13
    countdown(3)  # 3, 2, 1, Done!
