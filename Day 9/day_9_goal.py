# TODO-1: Ask the user for input
import art

show_art = True

if show_art:
    print(art.logo)

my_dict = {}

is_repeat = True

while is_repeat:
    name = input("What's your name?: ")
    price = int(input("What is your bid: $"))

    # TODO-2: Save data into dictionary {name: price}
    my_dict[name] = price

    # TODO-3: Whether if new bids need to be added
    restart = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if restart == 'no':
        is_repeat = False
    else :
        print("\n" * 50)

# TODO-4: Compare bids in dictionary
max_bid = 0
max_bid_name = ""
for key in my_dict:
    if max_bid < my_dict[key]:
        max_bid = my_dict[key]
        max_bid_name = key

print(f"The winner is {max_bid_name} with bid {max_bid}")
