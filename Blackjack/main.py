import art
import random


def deal_card():
    """
    :return: return a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    :return: total score of the cards
    """
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def check_score(user, computer):
    """
    :param user: user score
    :param computer: computer score
    :return: statement
    """

    if user == computer:
        return "It's a draw :O"
    elif computer == 21:
        return "You lose. Opponent has Blackjack !"
    elif user == 21:
        return "You win with a Blackjack !"
    elif user > 21:
        return "You went over. You lose :("
    elif computer > 21:
        return "You win. Opponent went over 21 :D"
    elif user > computer:
        return "You win !"
    else:
        return "You lose ! :("

def blackjack():

    print(art.logo)
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    should_continue = True
    while user_score != 21 and user_score < 22 and should_continue:
        print("\n")
        print(f"Your cards = {user_cards}     Current score = {user_score}")
        print(f"Computer's first card = {computer_cards[0]}")

        choice = input("\nType 'y' to get another card, type 'n' to pass : ")

        if choice == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)

        elif choice == 'n':
            should_continue = False

    print("\n")
    print(f"Your final hand = {user_cards}     Final score = {user_score}")
    print(f"Computer final hand = {computer_cards}     Final score = {computer_score}")

    print(f"\n{check_score(user_score, computer_score)}\n")


while input("Do you want to play Blackjack? Type 'y' or 'n' : ") == 'y':
    print("\n" * 20)
    blackjack()
