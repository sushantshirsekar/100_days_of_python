from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine
import time

coffee_maker = CoffeeMaker()
coffee_menu = Menu()
money_class = MoneyMachine()
menu_list = "/".join(coffee_menu.get_drinks())

while True:
    print("\n" * 5)
    get_user_coffee = input(f"What would you like? {menu_list}:  ")
    if get_user_coffee.lower() == 'off':
        break
    elif get_user_coffee.lower() == 'report':
        coffee_maker.report()
        money_class.report()
        time.sleep(5)
        continue
    user_coffee = coffee_menu.find_coffee(get_user_coffee)

    if user_coffee is not None:
        is_pay_success = money_class.make_payment(user_coffee.cost)
        if is_pay_success:
            coffee_maker.make_coffee(user_coffee)
            time.sleep(5)
        else:
            time.sleep(5)
            continue

    else:
        continue


