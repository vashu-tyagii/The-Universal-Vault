"""pathlib: object-oriented filesystem paths.

Why use pathlib?
	``Path`` objects are easier to read than string-based path operations and
	work across Windows, macOS, and Linux.

Important ideas
---------------
* ``Path.cwd()``      - current working directory
* ``Path.home()``     - current user's home directory
* ``/``               - safely joins path parts
* ``exists()``        - whether a path exists
* ``is_file()``       - whether a path is a file
* ``is_dir()``        - whether a path is a directory
* ``name``            - final name, including extension
* ``stem``            - final name without extension
* ``suffix``          - final extension, such as ``.txt``
* ``parent``          - containing directory

Useful methods
--------------
``mkdir(parents=True, exist_ok=True)`` creates directories.
``write_text()`` and ``read_text()`` work with text files.
``write_bytes()`` and ``read_bytes()`` work with binary files.
``iterdir()`` lists direct children; ``glob()`` and ``rglob()`` find matches.
``rename()`` moves or renames a path, while ``unlink()`` deletes a file.

Run this file from any directory.  The example creates its files in a
temporary directory and removes that directory automatically afterwards.
"""

from pathlib import Path
from tempfile import TemporaryDirectory


def pathlib_example() -> None:
    """Demonstrate common pathlib operations."""
    project_dir = Path.cwd()
    print(f"Current directory: {project_dir}")

    with TemporaryDirectory() as temporary_directory:
        workspace = Path(temporary_directory) / "workspace"
        workspace.mkdir(parents=True, exist_ok=True)

        notes_file = workspace / "notes.txt"
        notes_file.write_text(
            "Learn pathlib\nUse Path objects\n", encoding="utf-8")

        print(f"File exists: {notes_file.exists()}")
        print(f"Is a file: {notes_file.is_file()}")
        print(f"Name: {notes_file.name}")
        print(f"Stem: {notes_file.stem}")
        print(f"Suffix: {notes_file.suffix}")
        print(f"Parent: {notes_file.parent}")
        print("Contents:")
        print(notes_file.read_text(encoding="utf-8"), end="")

        (workspace / "data.csv").write_text("id,value\n1,100\n", encoding="utf-8")
        print("Text files:", [path.name for path in workspace.glob("*.txt")])
        print("All files:", [path.name for path in workspace.iterdir()])

        renamed_file = workspace / "renamed-notes.txt"
        notes_file.rename(renamed_file)
        print(f"Renamed path: {renamed_file}")


if __name__ == "__main__":
    pathlib_example()
