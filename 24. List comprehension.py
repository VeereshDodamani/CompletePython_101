## List comprehension : A concise way to create lists in python
#                       compact and easy to read than traditional loop
#                       [expression for value in iterable if condition]

# normal way to create a list
print("By using normal way")
doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

# using the comperhension
print("By using comperhension")
doubles = [x*2 for x in range(1,11)]
print(doubles)

fruits = ["apple","banana","watermelon","pineapple"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruits = [fruit.upper() for fruit in ["apple","banana","watermelon","pineapple"]]
print(fruits)

fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

nums = [-2,-5,8,9,-4,2,7,0,-6,1]
pos_num = [number for number in nums if number>=0]
print(pos_num)

neg_num = [number for number in nums if number<0]
print(neg_num)

grades = [45,23,56,67,18,89,34,90,24,97]
passing_grades = [grade for grade in grades if grade>36]
print(passing_grades)
