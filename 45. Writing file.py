# Python writing files (.txt, .json, .csv)

txt_data = "We go JIM"
# file name
file_path = "output.txt"
# path of flie
file_path = "C:/User/HP/Desktop/output.txt"

# w -> write
# x -> if file dosen't exist
# a -> appending text

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created.")
