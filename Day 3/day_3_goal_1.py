# ===================================================
# Script-Purpose : Calculates total pizza bill based
# on size and add-ons.
# ===================================================

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_bill = 0
if size.lower() == 's':
    total_bill = total_bill +  15
    if pepperoni.lower() == 'y':
        total_bill = total_bill + 2
    if extra_cheese.lower() == 'y':
        total_bill = total_bill + 1
elif size.lower() == 'm' :
    total_bill = total_bill + 20
    if pepperoni.lower() == 'y':
        total_bill = total_bill + 3
    if extra_cheese.lower() == 'y':
        total_bill = total_bill + 1
elif size.lower() == 'l' :
    total_bill = total_bill + 25
    if pepperoni.lower() == 'y':
        total_bill = total_bill + 3
    if extra_cheese.lower() == 'y':
        total_bill = total_bill + 1
else:
    print('''We don't have a pizza of your choice!''')

print('Your final bill is: $' + str(total_bill)+'.')
