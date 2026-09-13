"""Global and local scope in Python.

Notes
-----
* A global variable is defined outside a function and can be read inside it.
* A local variable is created inside a function and exists only during that call.
* Assigning to a name inside a function makes it local by default.
* Use ``global`` only when a function must reassign a module-level variable.
* Prefer returning values and passing arguments instead of changing global state.
* ``nonlocal`` is used by a nested function to reassign a variable in its
  enclosing function (not a module-level variable).
    It lets the nested function update that enclosing variable instead of
    creating a new local variable.
"""

message = "global value"


def read_global():
    """A function may read a global value without declaring it global."""
    return message


def local_example():
    """Variables assigned here are local to this function."""
    message = "local value"
    return message


def update_global():
    """The ``global`` keyword allows reassignment of the global variable."""
    global message
    message = "updated global value"


def make_counter():
    """Return a closure that updates an enclosing local variable.

    ``nonlocal count`` means that ``counter`` changes the ``count`` belonging
    to ``make_counter`` rather than creating a separate local ``count``.
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


if __name__ == "__main__":
    print("Before update:", read_global())
    print("Local value:", local_example())
    print("Global value outside function:", message)

    update_global()
    print("After update:", message)

    next_count = make_counter()
    print("Counter:", next_count())
    print("Counter:", next_count())
