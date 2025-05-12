## Dictionary = a collection of {key:value} pairs, ordered and changeable. No duplicates

capitals = {"India":"Delhi","USA":"Washington","China":"Beijing","Russia":"Moscow"}
print("Printing DICTIONARY")
print("'Key':'Value'")
print(capitals)

# printing a particular value of a key
print("Printing a particular value of a key")
print(capitals.get("India"))
print("\n")

# If statement
print("IF Statement")
if capitals.get("Japan"): # Russia, Mexico
    print("That capital does exist in dictionary")
else:
    print("That capital doesn't exist")
print("\n")

# Updating the dictionary
print("Updating the dictionary")
capitals.update({"Genmany":"Berlin"})
print(capitals)
print("\n")

# changing the value
print("Changing the value of a key")
capitals.update({"USA":"Detroit"})
print(capitals)
print("\n")

# Remove the last element
print("Remove the last element")
capitals.popitem()
print(capitals)
print("\n")

# Remove the particular element
print("Remove the particular element")
capitals.pop("China")
print(capitals)
print("\n")

# Print all the key present in the dictionary
print("Print all the key present in the dictionary")
print(capitals.keys())
print("Using for loop to get keys ")
for i in capitals.keys():
    print(i)
print("\n")

# Print all the values present in the dictionary
print("Print all the values present in the dictionary")
print(capitals.values())
print("Using for loop to get values  ")
for i in capitals.values():
    print(i)
print("\n")



# Clear the dictionary
print("Clear the dictionary")
capitals.clear()
print(capitals)
print("\n")
