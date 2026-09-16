"""
File handling: read, create, open, update, insert and delete data.
Examples function ke bina diye gaye hain.
"""

# ==========================================================
# Method 1: with open(...) - recommended
# File automatically close ho jaati hai.
# ==========================================================

# CREATE / WRITE: file banao aur data likho
with open("notes.txt", "w") as file:
	file.write("Apple\n")
	file.write("Mango\n")

# READ: poori file read karo
with open("notes.txt", "r") as file:
	data = file.read()
	print(data)

# OPEN aur line-by-line read
with open("notes.txt", "r") as file:
	for line in file:
		print(line.strip())

# UPDATE: purana data replace karke naya data likho
with open("notes.txt", "w") as file:
	file.write("Apple updated\n")
	file.write("Mango\n")

# INSERT / ADD: file ke end me data add karo
with open("notes.txt", "a") as file:
	file.write("Banana\n")

# DELETE DATA: jis line ko delete karna hai, use chhodkar baaki save karo
with open("notes.txt", "r") as file:
	lines = file.readlines()

with open("notes.txt", "w") as file:
	for line in lines:
		if line.strip() != "Mango":
			file.write(line)

# ==========================================================
# Method 2: open(...) aur close() manually
# ==========================================================

# CREATE / WRITE
file = open("example.txt", "w")
file.write("First line\n")
file.write("Second line\n")
file.close()

# READ
file = open("example.txt", "r")
data = file.read()
print(data)
file.close()

# UPDATE: "w" purana data hata kar naya data likhta hai
file = open("example.txt", "w")
file.write("Updated line\n")
file.close()

# INSERT / ADD: "a" end me data add karta hai
file = open("example.txt", "a")
file.write("Added line\n")
file.close()

# DELETE DATA: line filter karke file dobara write karo
file = open("example.txt", "r")
lines = file.readlines()
file.close()

file = open("example.txt", "w")
for line in lines:
	if line.strip() != "Added line":
		file.write(line)
file.close()

# Modes:
# "r" = read, "w" = write/create (purana data delete),
# "a" = append/insert at end, "x" = sirf new file create,
# "r+" = read aur write dono.
