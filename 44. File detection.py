# python file detection

import os

file_path = "C:/User/HP/Desktop/test.txt"
#file_path = "test.txt"
if os.path.exists(file_path):
    print(f"The location {file_path} exist.")

    # To check if it is a file, not a directory
    if os.path.isfile(file_path):
        print("That is a file.")

    # To check if it is a directory
    elif os.path.isdir(file_path):
        print("That is a directory.")
else:
    print(f"The location {file_path} doesn't exist.")
