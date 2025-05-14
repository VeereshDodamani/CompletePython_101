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
