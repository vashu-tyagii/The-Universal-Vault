"""File handling in Python
==========================

Notes
-----
* ``open(path, mode, encoding="utf-8")`` opens a file.
* Prefer ``with open(...)`` because it closes the file automatically.
* Common modes:
  - ``"r"`` read (default; the file must exist)
  - ``"w"`` write (creates or overwrites the file)
  - ``"a"`` append (creates the file if needed)
  - ``"x"`` create exclusively (fails if the file exists)
  - Add ``"b"`` for binary files, such as ``"rb"`` or ``"wb"``.
* ``read()`` reads all content, ``readline()`` reads one line, and
  ``readlines()`` returns a list of lines.
* Iterating over a file is memory-efficient for large files.
* Use ``encoding="utf-8"`` for predictable text handling.
"""

from pathlib import Path


def file_handling_example() -> None:
    """Create, write, read, append, and delete a text file."""
    file_path = Path("example.txt")

    # Write: creates the file or replaces its contents.
    with file_path.open("w", encoding="utf-8") as file:
        file.write("First line\n")
        file.write("Second line\n")

    # Read the complete file.
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    print(content)

    # Append without removing existing content.
    with file_path.open("a", encoding="utf-8") as file:
        file.write("Added later\n")

    # Read one line at a time (useful for large files).
    with file_path.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line.rstrip()}")

    # Check before deleting to avoid FileNotFoundError.
    if file_path.exists():
        file_path.unlink()


def read_existing_file(file_path: str) -> list[str]:
    """Return non-empty, stripped lines from an existing text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return []


if __name__ == "__main__":
    file_handling_example()
