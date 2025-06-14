# Python reading files (.txt, .json, .csv)

file_path = "C:/User/HP/Desktop/file.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
