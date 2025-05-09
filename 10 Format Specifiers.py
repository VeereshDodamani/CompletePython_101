## Format Specifier : {value:flags} format a value based on what flags are inserted

# .(number)f = rpund to that many decimal places (fixed points)
# :(numbers) = allocate that many spaces
# :03 = allocate and zero pad that many values
# :< = left justify
# :> = right justify
# :^ = center aligned
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
#, = comma separator

price1 =  3.14543
price2 = -9.3546
price3 = 12.3429

print(f"Price 1  is: {price1}")
print(f"Price 2  is: {price2}")
print(f"Price 3  is: {price3}")
print('\n')

# To get decimal points : 2f means 2 decimal points
print("2 decimal points")
print(f"Price 1  is: {price1: .2f}")
print(f"Price 2  is: {price2: .2f}")
print(f"Price 3  is: {price3: .2f}")
print('\n')

# Each value now have total of 10 spaces
print("10 spaces")
print(f"Price 1  is: {price1: 10}")
print(f"Price 2  is: {price2: 10}")
print(f"Price 3  is: {price3: 10}")
print('\n')

# Each value will be zero padded
print("zero padded")
print(f"Price 1  is: {price1: 010}")
print(f"Price 2  is: {price2: 010}")
print(f"Price 3  is: {price3: 010}")
print('\n')

# All are left justified
print("Left Justified")
print(f"Price 1  is: {price1: <10}")
print(f"Price 2  is: {price2: <10}")
print(f"Price 3  is: {price3: <10}")
print('\n')

# All are right justified
print("Right Justified")
print(f"Price 1  is: {price1: >10}")
print(f"Price 2  is: {price2: >10}")
print(f"Price 3  is: {price3: >10}")
print('\n')

# All are center aligned
print("Center Aligned")
print(f"Price 1  is: {price1: ^10}")
print(f"Price 2  is: {price2: ^10}")
print(f"Price 3  is: {price3: ^10}")
print('\n')
