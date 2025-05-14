# *args = allows to pass multiple non-key arguments
# **kwargs = allows to pass multiple keywords arguments
#            * unpacking arguments
#            1. positional, 2.default, 3.keyowrds, 4. Arbitrary


def add(a,b):
    return a+b
print(add(1,2))

# We can't give more than 2 args for the add function
# So the solution is to pass *args, which will convert the values into tuples

def add(*nums): # *nums is the unpacking operator
    print(type(nums))
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3))
print(add(1))
print(add(1,2,3,4))
print(add(1,2,3,5,6))


def display_name(*name):
    for nam in name:
        print(nam, end=" ")
display_name("Dr.","Hari","Prasad","III")


# **keargs conver the arguments into dictionaries
def print_adderess(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_adderess(street="123 Fake Str",
      city="Banglore",
      state="Washing_ton",
      zip="354798")


def shipping_label(*args, **kwargs):
    for name in args:
        print(name, end=" ")
    print("\n")
    
    for key, value in kwargs.items():
        print(f"{key} : {value}")

shipping_label("Dr.","Hari","Prasad",
               street = "123 Fake road",
               city = "Anom City",
               pin = "431209")
