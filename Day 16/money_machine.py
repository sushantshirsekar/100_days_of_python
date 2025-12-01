class MoneyMachine:
    CURRENCY = "$"

    COINS = {
        "Quarters" : 0.25,
        "Dimes" : 0.10,
        "Nickles" : 0.05,
        "Pennies" : 0.01,
    }

    def __init__(self):
        self.money_received = 0
        self.total_profit = 0

    def report(self):
        """Prints Total Profit collected."""
        print(f"Total Profit :{self.CURRENCY}{self.total_profit}")

    def process_coins(self):
        print("Please Insert Coins:")
        for i in self.COINS:
            self.money_received += int(input(f"How much {i}? ")) * self.COINS[i]
        return self.money_received


    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost and self.money_received > 0:
            change = round(self.money_received - cost , 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.total_profit += cost
            self.money_received = 0
            return True
        else :
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
