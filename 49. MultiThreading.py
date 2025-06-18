# MultiTheading = MultiTheading is used to perform moltiple task cocurrently (Multitasking)
#                 Good for input/output bound task like reading files / fetching data from APIs #                 threading. Thread(target = my_function)

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")

def take_out_trash():
    time.sleep(6)
    print("Take out the trash.")

def get_mail():
    time.sleep(3)
    print("You will get the mail")

# what it does is
# once when the time starts, after 3 sec take_out_trash() will be execuated, after 5 sec get_mail() and then after 10 sec walk_dog
# time won't start from beginning after every function

# to pass a argument
chore1 = threading.Thread(target=walk_dog, args=("Scooby",)) # pass it as tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chore's completed")
