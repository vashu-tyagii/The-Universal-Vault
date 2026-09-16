"""Writing to and creating files in Python.

Notes:
	- open() returns a file object and accepts a path and a mode.
	- "w" creates a file or replaces its existing contents.
	- "a" creates a file if needed and appends to its contents.
	- "x" creates a new file and raises FileExistsError if it already exists.
	- "r+" allows reading and writing without deleting existing contents.
	- Add "b" to a mode when working with binary data, such as images.
	- Use a with statement so the file is closed automatically, even on errors.
	- write() writes one string; writelines() writes an iterable of strings.
	- Newline characters (\n) must be included when separate lines are needed.

The examples below use a file in the current directory.  In real projects,
prefer pathlib.Path for platform-independent paths.
"""

from pathlib import Path


file_path = Path("example.txt")


# 1. Create a file and write text to it.
# Mode "w" creates the file or overwrites it if it already exists.
with file_path.open("w", encoding="utf-8") as file:
	file.write("First line\n")
	file.write("Second line\n")


# 2. Append text without replacing the existing contents.
with file_path.open("a", encoding="utf-8") as file:
	file.write("A line added later\n")


# 3. Write several lines at once.
lines = ["Python\n", "makes\n", "file handling\n", "simple.\n"]
with file_path.open("w", encoding="utf-8") as file:
	file.writelines(lines)


# 4. Create a file only when it does not already exist.
try:
	with file_path.open("x", encoding="utf-8") as file:
		file.write("This is a new file.\n")
except FileExistsError:
	print(f"{file_path} already exists.")


# 5. Check that the file exists and display its size.
if file_path.exists():
	print(f"Created: {file_path.resolve()}")
	print(f"Size: {file_path.stat().st_size} bytes")
