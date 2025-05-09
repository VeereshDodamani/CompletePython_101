## While loop = executes some code while some condition remains true

# If statement
name = input("Enter your name: ")
if (name == ""):
    print("You didn't enter anything....")
else:
    print(f"Hello, {name}")

# While statement
# Ask the user to enter name, till he dosen't enter name
while name == "":
    print("plz, write your name...")
    name = input("Enter your name: ")
print(f"Hello, {name}")


age = int(input("Enter your age: "))
while age<=0:
    print("Age dosen't exist like this.")
    age = int(input("Enter your age: "))
print(f"Your age is : {age}")


food = input("Enter a food you like (press q to exit): ")
print(f"You like : {food}")

while food!="q":
    food = input("Enter a food you like (press q to exit): ")
    print(f"You like : {food}")

print("Out of WHILE loop")
