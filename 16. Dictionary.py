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
