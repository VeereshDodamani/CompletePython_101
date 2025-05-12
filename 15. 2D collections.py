## 2D collections = elements are present in 2 dimensions, normally list, set or tuple is 1 dimensional. 
##                  Collections of list/set/tuple is called as 2D collection

fruits = ["apple","banana","orange","mango","pineapple"]
veggies = ["carrot","palak","potato","onion","coliflower"]
meat = ["chicken","fish","beef","rabbit","camel"]

# printing 1D list
print("Fruits")
print(fruits)
# changing 1D list element
print("Changing a 1D list")
fruits[1]="muskmelon"
print(fruits)

# creating a 2D list
print("Creating a 2D collection of list")
groceries = [fruits, veggies, meat]
# printing 2D list
print(groceries)

# changing 2D list element
print("To select a element in 2D list, consider the row and column number of it.")
print("Changing a 2D element")
groceries[0][1] = "kiwi"
print(groceries)

# for loop in 2D colletion
print("For loop in 2D collection")
for collection in groceries:
    print(collection)

# nested loop in 2D collection
# to select individual element 
print("Nested loop in 2D collection")
for collection in groceries:
    for element in collection:
        print(element)
