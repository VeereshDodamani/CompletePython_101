# Hangman in python

import random

words = ("apple","orange","banana","coconut","pineapple","mango","grape","strawberry","blueberry","kiwi","papaya","peach","watermelon","cherry","pomegranate")
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


# # Checking if the dictionary is working
# print("Checking if the dictionary is working")
# for line in hangman_art[6]:
#     print (line)
# print("\n")

def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer): 
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    gussed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input....")
            continue

        if guess in gussed_letters:
            print(f"{guess} is already guessed")
            continue

        gussed_letters.add(guess)

    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOOSE")
            is_running = False
 

if __name__ == "__main__":
    main()
