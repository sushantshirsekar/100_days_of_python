class MenuItem():
    def __init__(self, name, cost, milk, water, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "milk" : milk,
            "water" : water,
            "coffee" : coffee
        }



class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_drinks(self):
        """Returns all the names of the available menu items"""
        options = []
        for item in self.menu:
            options.append(str(f"{item.name}"))
        return options

    def find_coffee(self, coffee_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""

        for i in self.menu:
            if str(i.name) == str(coffee_name).lower():
                return i
        print("Sorry that item is not available.")
        return None

