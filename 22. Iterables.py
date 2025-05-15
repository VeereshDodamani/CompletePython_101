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
