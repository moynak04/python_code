MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def print_report():
    """Print the current resources and money."""

    print("\n========== MACHINE REPORT ==========")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")
    print("====================================\n")


def check_resources(drink):
    """Check whether there are enough ingredients to make the drink."""

    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def get_valid_coin(prompt):
    """Get a valid non-negative integer from the user."""

    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter 0 or a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def process_coins():
    """Collect coins and return the total money inserted."""

    print("\nPlease insert coins.")

    quarters = get_valid_coin("How many quarters? ")
    dimes = get_valid_coin("How many dimes? ")
    nickels = get_valid_coin("How many nickels? ")
    pennies = get_valid_coin("How many pennies? ")

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    return total


def make_coffee(drink):
    """Deduct the required ingredients from the machine."""

    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]


def get_drink_choice():
    """Ask the user for a valid drink choice."""

    while True:
        choice = input(
            "What would you like? "
            "(espresso/latte/cappuccino): "
        ).lower().strip()

        if choice in MENU:
            return choice

        if choice == "report":
            return "report"

        if choice == "off":
            return "off"

        print(
            "Invalid choice. Please enter "
            "espresso, latte, cappuccino, report, or off."
        )


# =========================
# MAIN COFFEE MACHINE
# =========================

machine_on = True

while machine_on:

    choice = get_drink_choice()

    # Turn machine off
    if choice == "off":
        print("\nCoffee machine shutting down...")
        machine_on = False
        continue

    # Print report
    if choice == "report":
        print_report()
        continue

    # Check resources
    if not check_resources(choice):
        continue

    # Get the price
    price = MENU[choice]["cost"]

    print(f"\n{choice.title()} costs ${price:.2f}")

    # Process payment
    payment = process_coins()

    print(f"Money inserted: ${payment:.2f}")

    # Check if enough money was inserted
    if payment < price:
        print(
            f"Sorry, that's not enough money. "
            f"${payment:.2f} refunded."
        )
        continue

    # Calculate change
    change = payment - price

    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    # Add money to machine
    money += price

    # Make the coffee
    make_coffee(choice)

    # Successful purchase
    print(f"Here is your {choice} ☕. Enjoy!")

print("\nThank you for using the Coffee Machine!")