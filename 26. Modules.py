## Module : a file containg code that you want to include in your program
#           use 'import' to include a module
#           useful to break a large program reusable seprate file

# print(help("modules"))

# importing math module
import math
print(f"Pi value from the module: ", math.pi)

# another way to import midule
# import as some other name
import math as mat
print(f"Pi value from the module: ", mat.pi)


# importing a particular value
from math import e
a,b,c,d = 1,2,3,4
print(f"a ** e: ", a**e)
print(f"b ** e: ", b**e)
print(f"c ** e: ", c**e)
print(f"d ** e: ", d**e)
print("\n")

# we are assigning e as 5, so now the value of e will be 5 not exponential value
a,b,c,d,e = 1,2,3,4,5
print(f"a ** e: ", a**e)
print(f"b ** e: ", b**e)
print(f"c ** e: ", c**e)
print(f"d ** e: ", d**e)
print(f"e ** e: ", e**e)

# You can aso create your own module and import it 
