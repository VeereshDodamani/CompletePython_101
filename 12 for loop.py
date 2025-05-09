## for loop : for loop will execute the block of code for fixed number of times.
#             You can iterate over a range, string, sequence etc.

# Print 10 first numbers, 11 because last digit is excluded
print("First 10 numbers: ")
for x in range(1,11):
    print(x)
print("\n")

# Print reversed 10 numbers
print("Reveresd numbers: ")
for x in reversed(range(1,11)):
    print(x)
print("\n")


# Step = 2, which mean print the next 2nd number
print("Skipping the next number: ")
for x in range(1,11,2):
    print(x)
print("\n")

# Continue word = continue word will skip over the iteration
print("Continu:e")
for i in range(1,21):
    if i == 13: # Now this will skip 13
        continue
    else:
        print(i)
print("\n")

# Break word = Break word will stop the itteration at that condition
print("Break:")
for i in range(1,21):
    if i == 13: # Now this will skip 13
        break
    else:
        print(i)
