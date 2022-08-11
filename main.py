MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


def prep(choice):
    global should_continue
    res_avail = check_resources(choice)

    if res_avail:
        # prompt to insert coins
        coin_insert(choice)
    else:
        should_continue = False

    return should_continue


def coin_insert(choice):
    print("Please insert coins")
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies? "))
    qtrs = float(input("How many qtrs?: "))

    tot_coins = (qtrs*.25) + (dimes*.10) + (nickels*.05) + (pennies * .01)

    if tot_coins >= MENU[choice]["cost"]:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        change = round(tot_coins - MENU[choice]["cost"], 2)
        resources["money"] += MENU[choice]["cost"]
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {choice} ☕ .")
    else:
        print("Sorry that's not enough money. Money refunded")
        # should_continue = False
        return


def check_resources(choice):
    enough_resources = True
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry not enough water available")
    elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry not enough milk available")
    elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry not enough coffee available")
    else:
        enough_resources = True
        return enough_resources


# TODO 1: Prompt user "WHat would you like? (espresso,latte, cappuccino)


should_continue = True

while should_continue:
    choice = input("What would you like? (espresso, latte, cappuccino): ")

    if choice == "off":
        should_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: ${resources['money']}.")

    else:
        should_continue = prep(choice)

# TODO 2: Check the user's input to decide what to do next


# TODO 3: The prompt should show every time an action is completed. Loop the program
# TODO 4: Turn off the coffee machine by turning entering "off" at the prompt.
# TODO 5: Print report that will show the current resource values
# TODO 6: Check resources sufficient?
# TODO 6.1: Before preparing the drink, it should check for resources
# TODO 6.2: If not enough, print message " Sorry, there is not enough {resource}
# TODO 7: Process coins. Once resources are checked and available, prompt the user to insert coins
# TODO 7.1: Only Qtrs(0.25), Dimes(0.10), nickels(0.05) and pennies(0.01) can be entered
# TODO 7.2: Calculate the value and if enough for the chosen drink, deliver the drink
# TODO 7.3: If not enough value for the drink, then refund the coins with the message " Sorry not enough
# TODO 7.3: money. Money refunded"
# TODO 8: If enough money, then the amount is added for the machine and will be reflected in the report
# TODO 8.1: If the user has inserted more money, then machine will offer change. "Here's the $x.xx in
# TODO 8.1: change" Change should be rounded to 2 decimal places
# TODO 9: Once everything is set, the ingredients should be reduced from the resources
# TODO 10: Tell the user " Here's your {drink}



