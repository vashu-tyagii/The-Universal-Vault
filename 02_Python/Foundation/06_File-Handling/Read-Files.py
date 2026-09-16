"""Reading files in Python.

Notes:
	* ``open()`` returns a file object.
	* Use ``with open(...)`` so the file is closed automatically.
	* ``"r"`` is the default mode and means read text.
	* ``encoding="utf-8"`` makes the expected text encoding explicit.
	* ``read()`` reads the whole file, ``readline()`` reads one line, and
	  ``readlines()`` returns a list of lines.
	* Iterating over a file is memory-friendly for large files.
	* ``FileNotFoundError`` occurs when the path does not exist.

Example file (``notes.txt``)::

	Python makes file handling simple.
	Always close files when you are finished with them.
"""

from pathlib import Path


file_path = Path("notes.txt")


# Read the complete file at once.
try:
    with file_path.open("r", encoding="utf-8") as file:
        contents = file.read()
    print(contents)
except FileNotFoundError:
    print(f"File not found: {file_path}")


# Read a file line by line.  This is preferable for large files because
# it does not load the entire file into memory.
try:
    with file_path.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line.rstrip()}")
except FileNotFoundError:
    print(f"File not found: {file_path}")


# Other useful approaches:
# first_line = file.readline()       # Read one line
# all_lines = file.readlines()       # Read all lines into a list
# text = file_path.read_text(encoding="utf-8")  # pathlib shortcut
