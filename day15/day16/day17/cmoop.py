class CoffeeMaker:

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        ingredients = self.MENU[drink]["ingredients"]

        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def make_coffee(self, drink):
        ingredients = self.MENU[drink]["ingredients"]

        for item in ingredients:
            self.resources[item] -= ingredients[item]

        print(f"Here is your {drink} ☕. Enjoy!")


class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def process_coins(self):
        print("Please insert coins.")

        total = 0

        for coin in self.COIN_VALUES:
            try:
                count = int(input(f"How many {coin}?: "))
            except ValueError:
                count = 0

            total += count * self.COIN_VALUES[coin]

        return total

    def make_payment(self, cost):
        money_received = self.process_coins()

        if money_received < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False

        change = round(money_received - cost, 2)

        if change > 0:
            print(f"Here is ${change} in change.")

        self.profit += cost

        return True


class Menu:

    def __init__(self):
        self.menu = CoffeeMaker.MENU

    def get_items(self):
        options = ""

        for item in self.menu:
            options += f"{item}/"

        return options


# Create objects
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:

    choice = input(
        f"What would you like? ({menu.get_items()}): "
    ).lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice in menu.menu:

        if coffee_maker.is_resource_sufficient(choice):

            drink_cost = menu.menu[choice]["cost"]

            if money_machine.make_payment(drink_cost):
                coffee_maker.make_coffee(choice)

    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")