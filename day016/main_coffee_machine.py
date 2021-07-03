from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# Documentation: https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_
# 43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

is_on = True

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        is_enough_ingredients = my_coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = my_money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            my_coffee_maker.make_coffee(drink)
