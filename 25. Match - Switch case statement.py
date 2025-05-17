## Match / Swith case statament : An alternative of using elif statement
#                                 Execute some code if value matches the case, that case will be executed
#                                 Benifit : Saves compliation time, clean and syntax is more readable

# if-elif compares all the possibility which takes more time
def day_of_week(day):
    if day == 1:
        print("It's MONDAY")
    elif day == 2:
        print("It's TUESDAY")
    elif day == 3:
        print("It's WEDNESDAY")
    elif day == 4:
        print("It's THURSDAY")
    elif day == 5:
        print("It's FRIDAY")
    elif day == 6:
        print("It's SATURDAY")
    elif day == 7:
        print("It's SUNDAY")
    else:
        print("Not a valid day")
day = int(input("Enter a day number in a week: "))
day_of_week(day)



# Match case will only compare with the particular case not all the possibilities
def day_of_week(day):
    match day:
        case 1:
            return "It's MONDAY"
        case 2:
            return "It's TUESDAY"
        case 3:
            return "It's WEDNESDAY"
        case 4:
            return "It's THURSDAY"
        case 5:
            return "It's FRIDAY"
        case 6:
            return "It's SATURDAY"
        case 7:
            return "It's SUNDAY"
        case _:
            return "Not a valid day"
        
day = int(input("Enter a day number in a week: "))
print(day_of_week(day))
