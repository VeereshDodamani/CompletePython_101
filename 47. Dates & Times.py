import datetime

# year-month-date
date = datetime.date(2025, 2,23)
print(f"Given date : {date}")

# To get todays date
today = datetime.date.today()
print(f"Todays date : {today}")

# hours:min:sec
time = datetime.time(23,23,23)
print(f"Given time : {time}")

current = datetime.datetime.now()
print(f"Current time and date : {current}")

# formatting the apperence
current = current.strftime("%H:%M:%S %m:%d:%y")
print(f"Formatted current date and time : {current}")

# Check if the current date and time have crossed the target date and time
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1) # year,month,date hours,min,sec
current_datetime = datetime.datetime.now()

if target_datetime<current_datetime:
    print("Passed the target date & time")
else:
    print("Not passed the target date and time")
