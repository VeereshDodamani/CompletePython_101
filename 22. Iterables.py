## Iterables : An objest/collection that can return it's element one at a time,
#              allowing it to be iterable over ina loop

# List are iterables
print("LISTS")
nums = [1,2,3,4,5]
for num in nums:
    print(num, end=" ")
print("\n")

for num in reversed(nums):
    print(num, end=" ")
print("\n")


# Tuples are iterables
print("TUPLES")
items = (1,2,3,4,5)
for item in items:
    print(item, end=" ")
print("\n")


# Sets are iterables but cannot perform any methods such as reversed
print("SETS")
fruits = {"apple","banana","mango","pineapple"}

for fruit in fruits:
    print(fruit)
print("\n")

for fruit in reversed(fruits):
    print(fruit)

# String's are iterable
print("STRINGS")
name = "Suryansh"

for char in name:
    print(char, end=" ")
print("\n")

for char in reversed(name):
    print(char, end=" ")

# Dict are iterables
my_dict = {"name":"Harsh","age":"23","place":"banglore"}

for key in my_dict:
    print(key)
print("\n")

# to get values of dict
for key in my_dict.values():
    print(key)
print("\n")

# to get both key and values
for key, values in my_dict.items():
    print(f"{key} = {values}")


email = "helloBro@yummy.com"

if "@" in email and "." in email:
    print(f"{email} is a VALID mail ID")
else:
    print(f"{email} is a NOT-VALID mail ID")
