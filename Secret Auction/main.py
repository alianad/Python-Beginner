from art import logo

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of $ {highest_bid}.")


print(logo)
print("Welcome to the auction program.")

bids = {}
bid_continue = True

while bid_continue:
    
    name = input("\nWhat is your name ? : ")
    price = int(input("What's your bid ? : $ "))
    bids[name] = price
    
    choice = input("\nAre there any other bidders? Type 'yes' or 'no' : ")
    if choice == 'no':
        bid_continue = False
        find_highest_bidder(bids)
