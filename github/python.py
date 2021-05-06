from dictionary import resources
from dictionary import MENU

espresso_cost = 1.50
latte_cost = 2.50
cappuccino_cost = 3.00

def current_resources():
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]

machine_on = True
while machine_on:
    print("Welcome to the Coffee Machine! ")

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("THIS MACHINE IS OFF.")
        machine_on = False
    elif choice == "report":
        print(f"The following ingredients are left: {resources}")
    elif (choice == "espresso" or choice == "latte" or choice == "cappuccino") and (resources["water"] < MENU[choice]["ingredients"]["water"] or resources["coffee"] < MENU[choice] ["ingredients"]["coffee"] or resources["milk"] < MENU[choice]["ingredients"]["milk"]):
        print("SORRY, THE MACHINE HAS RUN OUT OF INGREDIENTS. ")
        machine_on = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print("Please Insert Coins. ")

        q = float(input("How many quarters: ")) / 4
        d = float(input("How many dimes: ")) / 10
        n = float(input("How many nickels: ")) / 20
        p = float(input("How many pennies: ")) / 100

        money_inserted = q + d + n + p

        if choice == "espresso" and money_inserted >= espresso_cost:
            print(f"Here is your {choice}. Enjoy! ")
            change = str(round(money_inserted - espresso_cost, 2))
            print(f"Your change is {change}")
        elif choice == "espresso" and money_inserted <= espresso_cost:
            print("You do not have enough money to purchase this drink. ")
        elif choice == "latte" and money_inserted >= latte_cost:
            print(f"Here is your {choice}. Enjoy! ")
            change = str(round(money_inserted - latte_cost, 2))
            print(f"Your change is {change}")
        elif choice == "latte" and money_inserted <= latte_cost:
            print("You do not have enough money to purchase this drink. ")
        elif choice == "cappuccino" and money_inserted >= cappuccino_cost:
            print(f"Here is your {choice}. Enjoy! ")
            change = str(round(money_inserted - cappuccino_cost, 2))
            print(f"Your change is {change}")
        elif choice == "cappuccino" and money_inserted <= cappuccino_cost:
            print("You do not have enough money to purchase this drink. ")

        current_resources()
