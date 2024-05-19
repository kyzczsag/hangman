import random

def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_guess(already_guessed):
    while True:
        guess = input("Odgadnij literę: ").lower()
        if guess == "quit":
            print("Dziękujemy za grę! Do zobaczenia!")
            exit()
        elif len(guess) != 1 or not guess.isalpha():
            print("Proszę wpisać jedną literę.")
        elif guess in already_guessed:
            print("Ta litera została już odgadnięta. Spróbuj ponownie.")
        else:
            return guess

def hangman(word, lives=6):
    guessed_letters = set()
    wrong_guesses = set()

    while lives > 0:
        print("Stan gry: ", display_current_state(word, guessed_letters))
        print("Błędne litery: ", " ".join(wrong_guesses))
        print(f"Pozostałe życia: {lives}")

        guess = get_guess(guessed_letters | wrong_guesses)

        if guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Gratulacje! Odgadłeś słowo: {word}")
                break
        else:
            wrong_guesses.add(guess)
            lives -= 1

    if lives == 0:
        print(f"Przegrałeś! Słowo to: {word}")

def main():
    possible_words = ["Warsaw", "Paris", "Berlin", "Oslo", "London"]
    chosen_word = random.choice(possible_words)
    hangman(chosen_word)

main()
