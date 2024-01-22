from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on=True
Coffee=CoffeeMaker()
Menu_taken=Menu()
Money=MoneyMachine()
while is_on:
    asking=input('What would you like you to choose : (espresso/latte/cappuccino):\n')
    if asking=='off':
        is_on=False
    elif asking=='report':
        Coffee.report()
        Money.report()
    else:
        drink2=Menu_taken.find_drink(asking)
        if Coffee.is_resource_sufficient(drink2):
            Money.make_payment(drink2.cost)
            Coffee.make_coffee(drink2)
            
        else:
            print('we dont have enough resources Money refunded\n')