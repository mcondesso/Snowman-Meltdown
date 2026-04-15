"""
Snowman Meltdown game logic module.

This module contains the core functionality for the Snowman Meltdown game,
including selecting a random word, validating guesses, displaying game state,
and running the main game loop.
"""

import random
from stages import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Select a random word from the WORDS list.

    Returns:
        str: A randomly selected word.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the current snowman stage and the partially guessed word.

    Args:
        mistakes (int): Number of incorrect guesses made.
        secret_word (str): The word to guess.
        guessed_letters (set): Letters and numbers guessed so far.
    """
    print(STAGES[mistakes])
    text = "WORD: "
    if mistakes < len(STAGES) - 1:
        for letter in secret_word:
            if letter in guessed_letters:
                text += letter
            else:
                text += "_"
            text += " "
        print(text.rstrip(), "\n")


def is_word_guessed(secret_word, guessed_letters):
    """
    Check if all letters and numbers in the secret word have been guessed.

    Args:
        secret_word (str): The word to guess.
        guessed_letters (set): Letters and numbers guessed so far.

    Returns:
        bool: True if all characters in secret_word are guessed, else False.
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def is_guess_valid(guess):
    """
    Validate the player's guess.

    Args:
        guess (str): The player's input.

    Returns:
        bool: True if guess is a single alphanumeric character (letter or digit), else False.
    """
    return len(guess) == 1 and guess.isalnum()


def display_game_over(secret_word):
    """
    Display the game over message and reveal the secret word.

    Args:
        secret_word (str): The word that was to be guessed.
    """
    print("\nGame Over! The word was:", secret_word)
    print(STAGES[-1])


def display_game_won():
    """Display the congratulatory message when the player wins."""
    print("\nCongratulations, you saved the snowman!")


def play_game():
    """
    Run the main game loop for Snowman Meltdown.

    The player guesses letters or numbers until they either guess the word
    or reach the maximum number of mistakes allowed.
    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = set()

    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter or number: ").lower().strip()
        if not is_guess_valid(guess):
            print("Invalid guess! Please enter a single letter or number.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1
        else:
            if is_word_guessed(secret_word, guessed_letters):
                break

    if mistakes == len(STAGES) - 1:
        display_game_over(secret_word)
    else:
        display_game_won()
