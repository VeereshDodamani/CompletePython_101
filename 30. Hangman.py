# Hangman in python

import random

words = ("apple","orange","banana","coconut","pineapple")

# Dictionary of keys
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" 0 ",
                  "   ",
                  "   "),
               2:(" 0 ",
                  " | ",
                  "   "),
               3:(" 0 ",
                  "/| ",
                  "   "),
               4:(" 0 ",
                  "/|\\",
                  "   "),
               5:(" 0 ",
                  "/|\\ ",
                  "/  "),
               6:(" 0 ",
                  "/|\\ ",
                  "/ \\")}


# Checking if the dictionary is working
print("Checking if the dictionary is working")
for line in hangman_art[6]:
    print (line)
print("\n")
def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    gussed_letters = set()
    is_running = True
    


if __name__ == "__main__":
    main()
