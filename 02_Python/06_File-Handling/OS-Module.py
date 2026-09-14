"""
OS Module in Python
===================

The os module provides a way to interact with the operating system,
including working with files, directories, environment variables, and
processes.

Key points:
- os helps you manage files and folders.
- It is platform-independent for many common tasks.
- It is useful for creating, deleting, checking, and navigating files.

Common functions:
- os.getcwd()       -> get current working directory
- os.listdir()      -> list files/folders in a directory
- os.mkdir()        -> create a single directory
- os.makedirs()     -> create directories recursively
- os.remove()       -> delete a file
- os.rmdir()        -> delete an empty directory
- os.removedirs()   -> remove directories recursively
- os.rename()       -> rename or move a file/folder
- os.path.exists()  -> check if path exists
- os.path.join()    -> join directory and file names safely
- os.path.isdir()   -> check if a path is a directory
- os.path.isfile()  -> check if a path is a file
- os.walk()         -> traverse directory tree
- os.environ        -> access environment variables

Note:
For file and folder paths, os.path is often used together with os.
"""

import os

# 1) Get current working directory
print("Current working directory:", os.getcwd())

# 2) List files in a directory
print("\nFiles and folders in current directory:")
print(os.listdir())

# 3) Create a directory
# os.mkdir("demo_folder")
# Creates a single folder named demo_folder in the current directory

# 4) Create nested directories
# os.makedirs("demo_folder/sub_folder/inner_folder", exist_ok=True)
# Creates all missing folders in the path

# 5) Check if a path exists
path = "demo_folder"
print(f"\nDoes '{path}' exist?", os.path.exists(path))

# 6) Join path correctly
file_path = os.path.join("demo_folder", "sample.txt")
print("Joined path:", file_path)

# 7) Create a file in a directory
# with open(file_path, "w") as f:
#     f.write("Hello from OS Module example!\n")

# 8) Rename a file
# os.rename(file_path, os.path.join("demo_folder", "renamed_sample.txt"))

# 9) Remove a file
# os.remove(os.path.join("demo_folder", "renamed_sample.txt"))

# 10) Remove a directory
# os.rmdir("demo_folder")
# Only works for empty directories

# 11) Walk through a directory tree
print("\nDirectory tree walk:")
for root, dirs, files in os.walk("."):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    print("---")

# 12) Environment variables
print("\nUser home directory:", os.environ.get("USERPROFILE") or os.environ.get("HOME"))

# 13) Get file size
# if os.path.exists("demo_folder/sample.txt"):
#     print("File size:", os.path.getsize("demo_folder/sample.txt"))

# Example: full workflow
print("\nExample workflow:")
folder = "os_demo"
file_name = "notes.txt"
file_path = os.path.join(folder, file_name)

if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Python OS module example\n")
    file.write("This file was created using Python.\n")

print("File created:", os.path.exists(file_path))
print("File size:", os.path.getsize(file_path), "bytes")

# Clean up example (optional)
# os.remove(file_path)
# os.rmdir(folder)

print("\nSummary:")
print("The os module is useful for file, directory, and environment operations.")
print("Use it carefully when creating or deleting files and folders.")
