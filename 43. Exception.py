# Exception : An event that interupt the flow of event
#             (ZeroDivision, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# if the input is not number then this will crash
# num = int(input("Enter a number: "))
# print(1/num)

# to overcome that
try:
    num = int(input("Enter a number: "))
    print(1/num)
# if it is any string
except ValueError:
    print("Enter a valid input.")
# if it is 0
except ZeroDivisionError:
    print("You can't divide by 0.")
# finally will always be executed
finally:
    print("Thank you!")
