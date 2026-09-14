"""Directory management in Python.

Notes:
- ``pathlib.Path`` provides a readable, platform-independent API.
- ``mkdir(parents=True, exist_ok=True)`` creates nested directories safely.
- ``iterdir()`` lists immediate children; ``rglob()`` searches recursively.
- ``shutil.copy2()``, ``move()``, and ``rmtree()`` copy, move, and delete data.
  Use ``rmtree()`` carefully because it permanently removes a directory tree.
"""

from pathlib import Path
import shutil


def directory_management_example() -> None:
	"""Demonstrate common directory operations in a self-contained workspace."""
	workspace = Path("example_workspace")
	reports = workspace / "reports"
	archive = workspace / "archive"

	reports.mkdir(parents=True, exist_ok=True)
	archive.mkdir(exist_ok=True)

	report = reports / "summary.txt"
	report.write_text("Directory management example\n", encoding="utf-8")

	print("Workspace contents:")
	for item in workspace.iterdir():
		kind = "directory" if item.is_dir() else "file"
		print(f"- {item.name} ({kind})")

	text_files = list(workspace.rglob("*.txt"))
	print("Text files:", [path.name for path in text_files])

	copied_report = archive / report.name
	shutil.copy2(report, copied_report)
	shutil.move(copied_report, archive / "moved-summary.txt")

	# Delete only the example directory created above.
	shutil.rmtree(workspace)


if __name__ == "__main__":
	directory_management_example()
