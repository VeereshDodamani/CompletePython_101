# Membership operator : used to find weather a value is found in a sequence (string, list, tuple, set or dictionary etc)
#                       1. in
#                       2. not in

word = "BANANA"
# in statement
print("IN statement")
letter = input("Guess a word in a secret word: ")
if letter in word:
    print(f"{letter} is present in {word}")
else:
    print(f"{letter} not present in {word}")  

# not-in statement
print("NOT-IN statement")
if letter not in word:
    print(f"{letter} is not present in {word}")


students = ("hari","sham","ravi","sanju","mohan")

find = input("Enter a name to fing in collection: ")
if find in students:
    print(f"{find} is present in the collection.")
else:
    print(f"{find} not there in collection")
