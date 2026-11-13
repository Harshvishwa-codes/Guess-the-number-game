# guess-the-number-game

import random


def get_guess():
    """Get a valid guess from the player."""

    while True:
        user_input = input("\nEnter your guess (1-100) or Q to quit: ").strip()

        if user_input.lower() == "q":
            return None

        try:
            guess = int(user_input)

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def play_game():
    """Run one round of the guessing game."""

    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    print("\n================================")
    print("       GUESS THE NUMBER")
    print("================================")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:

        guess = get_guess()

        if guess is None:
            print("\nYou left the game.")
            return

        attempts += 1
        remaining = max_attempts - attempts

        if guess == secret_number:
            print("\nCongratulations! You guessed the number!")
            print(f"You won in {attempts} attempt(s).")
            return

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    print("\nGame over! You used all your attempts.")
    print(f"The correct number was: {secret_number}")


def main():
    """Main function of the program."""

    print("Welcome to Guess the Number Game!")

    while True:
        play_game()

        while True:
            choice = input("\nDo you want to play again? (y/n): ").strip().lower()

            if choice in ("y", "n"):
                break

            print("Invalid choice! Please enter y or n.")

        if choice == "n":
            print("\nThanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")

