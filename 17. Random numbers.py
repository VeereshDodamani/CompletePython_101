import random

# print(help(random)) # to know more methods about random

# to get a random number between 1-6
print("To get a random number between 1-6")
print(random.randint(1,6))

low = 1
high = 100
print(random.randint(low,high))

print("Floating number between 0-1")
print(random.random())

print("Rock, Paper, Scissors GAME")
options = ("Rock", "Paper", "Scissors")
print(random.choice(options))

