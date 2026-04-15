"""
Main entry point for the game application.

This module runs the main game loop, starting the game and prompting the user
to play again until they choose to exit.
"""

from game_logic import play_game


def main():
    """
    Run the main game loop.

    Starts the game by calling play_game() once, then repeatedly asks the user
    if they want to play again. Accepts only 'yes' or 'no' as valid input.
    If 'yes', the game restarts; if 'no', the program thanks the user and exits.
    """
    play_game()
    while True:
        answer = input("Would you like to play again? (yes/no) ").strip().lower()
        if answer not in {"yes", "no"}:
            print("Please enter 'yes' or 'no'.\n")
            continue
        elif answer == "yes":
            play_game()
        else:
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
