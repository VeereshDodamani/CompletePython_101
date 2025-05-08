## String Methods

name = input("Enter your name: ")
print("Lenght of your name is: ",len(name))

alp = input("Enter a aplhabet to find in name: ")

# If the alphabet is not present in name it will return -1
print("alphabet present at: ",name.find(alp))
print("Reverse occurance: ",name.rfind(alp))
print("Capitalized: ",name.capitalize())
print("Upper Case: ",name.upper())
print("Lower Case: ",name.lower())
print("Is the give word fullyy digits: ",name.isdigit())
print("Is the give word fullyy alphabetic: ",name.isalpha())

occurance = input("Enter a alphabet to count its occurance: ")
print(f"The occurance of {occurance} is: ", name.count(occurance))

replace_word = input("Enter a alphabet to replace in the Name: ")
print("After replacement: ", name.replace(replace_word,"X"))

# To know more about strings methods
print(help(str))
