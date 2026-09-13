"""Notes and examples for Python's ``pass`` statement.

``pass`` intentionally does nothing. It is useful as a placeholder when
Python requires an indented statement, such as in a function, class, loop,
or exception handler. Unlike a comment, it is a valid executable statement.

``pass`` is different from:
* ``continue``: skips to the next loop iteration.
* ``break``: exits the loop completely.
"""


# An empty function needs a statement in its body.
def feature_not_ready():
    pass


# It can also define an empty class for later use.
class UserTemplate:
    pass


# In a loop, pass does nothing; execution continues normally.
for number in range(3):
    pass


# A temporary exception handler can use pass intentionally.
try:
    result = 10 / 0
except ZeroDivisionError:
    pass


# Comparison with continue and break:
for number in range(5):
    if number == 1:
        pass       # Do nothing; the remaining body still runs.
    if number == 2:
        continue   # Skip to the next iteration.
    if number == 4:
        break      # Stop the loop.
    print(number)
