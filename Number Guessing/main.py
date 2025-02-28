import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("\n\tToo high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("\n\tToo low.")
        return turns - 1
    else:
        print(f"\nYou got it! The answer was {actual_answer}.")

def game():
    print(art.logo)

    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    lives = set_difficulty()

    guess = 0
    while guess != number:
        print(f"\nYou have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        lives = check_answer(guess, number, lives)
        if lives == 0:
            print("\nYou've run out of guesses. You lose !")
            return

game()
