## Collection = a single "variable" used to store multiple variables

## List = [] ordered and changeable. Duplicated ok
## Sets = {} unordered and immutable, but add/remove ok, no duplicates
## Tuples = () ordered and unchangable, Duplicates ok, faster

print("\n")
print("LIST'S")
fruits = ["Apple","Grapes","Watermelon","Pineapple","Mango"]
print(fruits)
print("\n")
print("INDEXING")
print(fruits[0])
print(fruits[1])
print(f"First 2 fruits: {fruits[0:2]}")
print(f"Last element: {fruits[-1]}")
print(f"Reverse: {fruits[::-1]}")
print("\n")
print("Using for loop")
for i in fruits:
    print(i)

# print(help(fruits)) 
print("Number of elements: ",len(fruits))
print(f"Does Apple exist in list: ", "Apple" in fruits)
print(f"Does Berry exist in list: ", "Berry" in fruits)
print("\n")

print("Changing the list elements")
fruits[1]="Mango"
print(fruits)
print("Adding element in list")
fruits.append("Coconut")
print(fruits)
print("To remove an element")
fruits.remove("Apple")
print(fruits)
print("Insert an element at a particular index")
fruits.insert(1, "Banana")
print(fruits)
print("Sort method")
fruits.sort()
print(fruits)
print("Reverse the list")
fruits.reverse()
print(fruits)
print("Find the index of an element")
print(fruits.index("Mango"))
print("Count the number of Mango")
print(fruits.count("Mango"))
print("To clear all the emements")
fruits.clear()
print(fruits)




print("\n")
print("SET'S")
cars = {"BMW","TATA","BENZ","JEEP"}
print(cars)
# print(help(cars))

print("Indexing dosen't apply on set because it is unordered")
print("Adding a element")
cars.add("PORSCHE")
print(cars)
print("Removing a element")
cars.remove("BMW")
print(cars)
print("Check if the element 'BMW' present in set")
print("BMW" in cars)
print("Duplicates not allowed")
cars.add("PORSCHE")
print(cars)
print("Pop the first element of the set")
cars.pop()
print(cars)
print("Clear the set")
cars.clear()
print(cars)
print("\n")


print("TUPLE'S")
names = ("Hari", "Prasad", "Rose", "Jack")
print(names)
# print(help(names))

print("Length of the tuple")
print(len(names))
print("Does RAM exist in names")
print("RAM" in names)
print("Finding the index of Prasad")
print(names.index("Jack"))
print("Finding the count of Hari")
print(names.count("Hari"))
print("Using for loop in the tuples")
for i in names:
    print(i)
