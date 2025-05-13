## Function = A block of resuable code
#             place () after the name to invoke it

# if i had to print this 3 times
# this is how i will do it normally
print("Happy Birthday To You")
print("How old are you?")
print("Happy Birthday To You")

print("Happy Birthday To You")
print("How old are you?")
print("Happy Birthday To You")

print("Happy Birthday To You")
print("How old are you?")
print("Happy Birthday To You")

# now let's do the same thing but using a function to print it 3 times
def happy_birthday():
    print("Happy Birthday To You")
    print("How old are you?")
    print("Happy Birthday To You")
    print("\n")


# invoking the function
happy_birthday()
happy_birthday()
happy_birthday()


# parameter : data which is given as argument, when it goes to function is called parameter
def happy_birthday(name):
    print(f"Happy Birthday To {name}")
    print("How old are you?")
    print(f"Happy Birthday To {name}")
    print("\n")


# arguments : any data you sent to a function is called arguments
happy_birthday("Bro")
happy_birthday("Steve")
happy_birthday("Jack")

# You can send more than 1 argument also
def age_printing(nam, age):
    print(f"Hello, {nam}")
    print(f"You are {age} years old!!!")

# Here I am sending name and age both
age_printing("Rahul", 30)
