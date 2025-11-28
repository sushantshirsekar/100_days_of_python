from data import MENU, resources
from art import logo
import time

def count_coins():
    total = (int(input("How much quarters?: ")) * 0.25)
    total +=  (int(input("How much dimes?: ")) * 0.10)
    total += (int(input("How much nickles?: ")) * 0.05)
    total += (int(input("How much pennies?: ")) * 0.01)
    return total

money = 0
while True:
    print("\n" * 20)
    print(logo)
    user_choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()

    if user_choice == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}kg")
        print(f"Money : ${money}")
        time.sleep(10)
        continue
    elif user_choice == "off":
        break

    is_ingredients = True
    for key in MENU[user_choice].get("ingredients"):
        if resources[key] < MENU[user_choice].get("ingredients").get(key):
            print(f"Insufficient {key.capitalize()}. Please choose other coffee.")
            is_ingredients = False

    if is_ingredients :
        is_money = True
        print("Please insert coins.")
        user_coins = count_coins()
        coffee_cost = MENU[user_choice].get("cost")
        if user_coins < coffee_cost:
            print(f"Sorry that's not enough money. Money refunded. ${user_coins}")
            is_money = False
        elif user_coins > coffee_cost:
            print(f"Here is ${user_coins - MENU[user_choice].get("cost")} dollars in change.")
            money += coffee_cost
        else:
            print(f"You inserted {user_coins}.")
            money += coffee_cost

        if is_money:
            for key in MENU[user_choice].get("ingredients"):
                resources[key] -= MENU[user_choice].get("ingredients").get(key)
            print(f"Here is your {user_choice.capitalize()}☕. Enjoy!")
        time.sleep(3)
