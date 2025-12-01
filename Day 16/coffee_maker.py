class CoffeeMaker:
    def __init__(self):
        self.resources={
            "milk" : 300,
            "water" : 200,
            "coffee" : 100,
        }

    def report(self):
        """Prints report of all resources."""
        print(f"Milk : {self.resources['milk']}ml")
        print(f"Water : {self.resources['water']}ml")
        print(f"Coffee : {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for i in drink.ingredients:
            if drink.ingredients[i] > self.resources[i]:
                return False
        return True

    def make_coffee(self, drink):
        """Deducts the required ingredients from the resources."""
        for i in drink.ingredients:
            self.resources[i] -= drink.ingredients[i]
        print(f"Here is your {drink.name} ☕️. Enjoy!")
