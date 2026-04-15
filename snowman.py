from game_logic import play_game


def main():
    play_game()
    while True:
        answer = input("Would you like to play again? (yes/no)").lower()
        if answer not in {"yes", "no"}:
            print("Please enter 'yes' or 'no'.\n")
            continue
        if answer == "yes":
            play_game()
        else:
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
