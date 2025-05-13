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
