MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def ask_for_order(coffee_chosen):
    if coffee_chosen == "report":
        return print_resources()
    elif coffee_chosen == "espresso":
        return compare_espresso_latte_cappuccino(coffee_chosen)
    elif coffee_chosen == "latte":
        return compare_espresso_latte_cappuccino(coffee_chosen)
    elif coffee_chosen == "cappuccino":
        return compare_espresso_latte_cappuccino(coffee_chosen)
    else:
        print("Come back when you want to drink coffee.")
        return True


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def compare_espresso_latte_cappuccino(coffee_chosen):
    water_needed = MENU[coffee_chosen]['ingredients']['water']
    beans_needed = MENU[coffee_chosen]['ingredients']['coffee']
    milk_needed = MENU[coffee_chosen]['ingredients']['milk']
    money_needed = MENU[coffee_chosen]['cost']
    if water_needed <= resources['water'] and beans_needed <= resources['coffee'] and milk_needed <= resources['milk']:
        insert_coins(money_needed, water_needed, beans_needed, milk_needed)
    elif water_needed > resources['water']:
        print("Sorry, not enough water.")
        return True
    elif milk_needed > resources['milk']:
        print("Sorry, not enough milk.")
        return True
    else:
        print("Sorry, not enough beans.")
        return True


def insert_coins(money_needed, water_needed, beans_needed, milk_needed):
    print("Please, insert coins!")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_coins = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if total_coins >= money_needed:
        calculate_change(total_coins, money_needed, water_needed, beans_needed, milk_needed)
    else:
        print(f"Sorry, not enough coins! The coffee cost ${money_needed}. Take yours ${total_coins} back.")
        return True


def calculate_change(total_coins, money_needed, water_needed, beans_needed, milk_needed):
    change = total_coins - money_needed
    final_change = "{:.2f}".format(change)
    if final_change == 0:
        resources_and_money(money_needed, water_needed, beans_needed, milk_needed)
        print("There is no change.")
        print(f"Here is your ☕ Enjoy!")
        return False
    else:
        resources_and_money(money_needed, water_needed, beans_needed, milk_needed)
        print(f"Here is ${final_change} in change.")
        print(f"Here is your ☕ Enjoy!")
        return False


def resources_and_money(money_needed, water_needed, beans_needed, milk_needed):
    resources['water'] -= water_needed
    resources['coffee'] -= beans_needed
    resources['milk'] -= milk_needed
    resources['money'] += money_needed


out_of_service = False

while not out_of_service:
    order = input("What would you like: espresso, latte or cappuccino? ").lower()
    out_of_service = ask_for_order(order)
