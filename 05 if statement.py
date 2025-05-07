## if : run's code only if the condition is true

age = int(input("Enter your age: "))

if (age>=18):
    print("Allowed to drive")

## if-else : if condition dosen't satisfies then else will be execuated

marks = float(input("Enter your marks: "))

if(age>15):
  print("You're allowed to go out")
else:
  print("No, not allowed")


## if-elif-else : If there are more than 2 conitions
marks = float(input("ENter your makrs: "))

if marks<35:
    print("Fail hai babu")
elif(35<marks<50):
    print("Pass, hoo gayu")
elif(50<marks<70):
    print("Distinction")
elif(70<marks<100):
    print("Distinction")
else:
    print("Invalid input")
