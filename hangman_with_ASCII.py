import os
import random

# Grafiki ASCII dla wisielca
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    -----------
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    -----------
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    -----------
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    -----------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    -----------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    -----------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    -----------
    """
]

def load_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(';')[0] for line in lines]

def display_current_state(word, guessed_letters):
    return " ".join([letter if letter.lower() in guessed_letters else "_" for letter in word])

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

def choose_level():
    while True:
        level = input("Wybierz poziom trudności (łatwy, średni, trudny): ").lower()
        if level in ["łatwy", "średni", "trudny"]:
            if level == "łatwy":
                return 10
            elif level == "średni":
                return 6
            elif level == "trudny":
                return 4
        else:
            print("Nieprawidłowy poziom trudności. Spróbuj ponownie.")

def hangman(words, lives):
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = set()

    while lives > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(hangman_stages[6 - lives])  # Wyświetla odpowiednią grafikę ASCII
        print("Stan gry: ", display_current_state(word, guessed_letters))
        print("Błędne litery: ", " ".join(wrong_guesses))
        print(f"Pozostałe życia: {lives}")

        guess = get_guess(guessed_letters | wrong_guesses)

        if guess in word.lower():
            guessed_letters.add(guess)
            if all(letter.lower() in guessed_letters for letter in word):
                print(f"Gratulacje! Odgadłeś słowo: {word}")
                break
        else:
            wrong_guesses.add(guess)
            lives -= 1

    if lives == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(hangman_stages[6 - lives])  # Wyświetla końcową grafikę ASCII
        print(f"Przegrałeś! Słowo to: {word}")

if __name__ == "__main__":
    words = load_words("countries-and-capitals.txt")
    lives = choose_level()
    hangman(words, lives)