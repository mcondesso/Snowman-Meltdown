import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    text = "WORD: "
    if mistakes < len(STAGES) - 1:
        for l in secret_word:
            if l in guessed_letters:
                text += l
            else:
                text += "_"
            text += " "
        print(text.rstrip(), "\n")


def display_game_over(secret_word):
    print("\nGame Over! The word was: ", secret_word)
    print(STAGES[-1])


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = set()
    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        guessed_letters.add(guess)
        if guess not in secret_word:
            mistakes += 1

    if mistakes == len(STAGES) - 1:
        display_game_over(secret_word)

    
if __name__ == "__main__":
    play_game()
