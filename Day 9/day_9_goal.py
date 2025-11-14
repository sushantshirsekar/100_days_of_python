# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    print(f"The winner is {winner} with bid {bidding_dictionary[winner]}")

bids = {}

should_continue = True

while should_continue:
    name = input("What's your name?: ")
    price = int(input("What is your bid: $"))

    bids[name] = price

    restart_input = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if restart_input == 'yes':
        print("\n" * 50)
    else :
        should_continue = False
        find_highest_bidder(bids)
