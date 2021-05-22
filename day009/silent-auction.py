from replit import clear
#HINT: You can call clear() to clear the output in the console. This works on the replit.com website
from art import logo

auction = {}

def pick_winner(bidding_dictionary):
    highest_bid = 0
    winner = ""
    # bidding_dictionary = {"Everson": 100, "Maria": 150, "Pereira": 201}
    for bidder in bidding_dictionary: # The for loop, in a dictionay, loops through the keys.
        bid_amount = bidding_dictionary[bidder] # bidding_dictionary[bidder] will give us the value
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def bidders_bid ():
    bidder_name = input("What is your name? ")
    bidder_price = int(input("What's your bid? $"))
    auction[bidder_name] = bidder_price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == 'yes':
        clear()
        bidders_bid()
    else:
        clear()
        pick_winner(auction)

print(logo)

print("Welcome to the secret auction program!")
bidders_bid()
