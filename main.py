from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_mc = CoffeeMaker()
coffee_menu = Menu()
#  coffee_menu_item = MenuItem()
money_mc = MoneyMachine()


def print_report():

    coffee_mc.report()
    money_mc.report()


should_continue = True


while should_continue:

    choice = input(f"What would you like? ({coffee_menu.get_items()}) : ")

    if choice == "off":
        should_continue = False
    elif choice == "report":
        print_report()
        #  should_continue = False
    else:
        item = coffee_menu.find_drink(choice)
        if item == None:
            should_continue = True
        else:
            if coffee_mc.is_resource_sufficient(item) and money_mc.make_payment(item.cost):
                coffee_mc.make_coffee(item)


