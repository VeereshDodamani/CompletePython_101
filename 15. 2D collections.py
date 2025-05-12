## 2D collections = elements are present in 2 dimensions, normal list, set or tuple is 1 dimensional. 
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
print("Changing a 2D element")
groceries[0][1] = "kiwi"
print(groceries)
