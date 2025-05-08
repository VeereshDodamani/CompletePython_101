# Conditional operators : a one line short cut for if-else statement 
#                         print or assign one or two values based on a condition
#                         x if condition else y

num = float(input("Enter a number: "))
print("Positive" if num>=0 else "Negative")
print("Even" if num%2==0 else "Odd")


age = int(input("ENter your age: "))
print("ALLOWED TO DRIVE" if age>18 else "NOT ALLOWED TO DRIVE")

temp = float(input("What's the weather: "))
print("It's HOT" if temp>30 else "It's not HOT")
