from random import choice
from art import logo, vs
from game_data import data


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(answer, followers_a, followers_b):
    if followers_a > followers_b:
        return answer == "A"
    else:
        return answer == "B"


score = 0
game_continue = True
account_b = choice(data)

print(logo)

while game_continue:

    account_a = account_b
    account_b = choice(data)

    if account_a == account_b:
        account_b = choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")

    followers_account_a = account_a["follower_count"]
    followers_account_b = account_b["follower_count"]
    guess = input("\nWho has more followers? Type 'A' or 'B' : ")

    print("\n" * 20)
    print(logo)
    if check_answer(guess, followers_account_a, followers_account_b):
        score += 1
        print(f"You're right ! Current score : {score}.")
    else:
        print(f"Sorry, that's wrong. Final score : {score}")
        game_continue = False
