import random

random.choice

def main():
    capitals = [
    "Paris", "Berlin", "Warsaw"
    ]

    lives = 3
    word_to_guess = random.choice(capitals).lower()
    display_word = "_ " * len(word_to_guess)
    good_guesses = set()
    while lives > 0 and "_" in display_word:
        print(f"Try guessing : {display_word}")
        letter = input("Try to guess a letter: ")
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




main()