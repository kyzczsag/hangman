import random

random.choice

def game(words: list, lives: int):
    word_to_guess = random.choice(words).upper()
    display_word = "_ " * len(word_to_guess)
    good_guesses = set()
    while lives > 0 and "_" in display_word:
        print(f"Try guessing : {display_word}")
        letter = input("Try to guess a letter: ").upper()
        if letter in word_to_guess:
            good_guesses.add(letter)
            display_word = ""
            for ch in word_to_guess:
                if ch in good_guesses:
                    display_word += ch
                else:
                    display_word += "_"
                display_word + " "
        else:
            lives -= 1
            if lives > 0:
                print(f"Wrong guess! You still have {lives} tries")
            else:
                print("You don't have any more tries")


    if lives > 0:
        print("You won!")
    else:
        print("You lost!")

def main():
    capitals = [
    "Paris", "Berlin", "Warsaw"
    ]
    lives = 3

    answer = input("Do you want to start a new game? Y/N ")
    while answer.lower() == "y":
        game(capitals, lives)
        answer = input("Do you want to start a new game? Y/N ")



main()