import os
def start():
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
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    def check_resources(asking):
        if asking in MENU:
            for _ in resources:
                if _ in MENU[asking]['ingredients']:
                    if MENU[asking]['ingredients'][_] > resources[_]:
                        return False
            return True
        else:
            return False
    def make_coffee():
        for x in resources:
            if x in MENU[asking]['ingredients']:
                resources[x] -= MENU[asking]['ingredients'][x]
        resources['money'] += MENU[asking]['cost']
        print(f'Your hot {asking} is ready sir! Have a pleasant coffee!')
    is_not_working=False
    resources['money']=0
    while not is_not_working:
        asking = input('What do u wish to have (espresso/latte/cappuccino): \n')
        if asking == 'report':
            for _ in resources:
                print(f'{_}={resources[_]}')
        elif asking == 'off':
            is_not_working=True
        else:
            if check_resources(asking):
                print('Please insert coins')
                quarters = int(input('Number of quarters\n'))
                dimes = int(input('Number of dimes\n'))
                penny = int(input('Number of pennies\n'))
                nickels = int(input('Number of nickels\n'))
                total_money = penny * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25
                if asking == 'espresso':
                    if total_money >= 1.5:
                        change_req = total_money - 1.5
                        print(f'change returned is {change_req}')
                    else:
                        print('The money is insufficient so Money refunded')
                elif asking == 'cappuccino':
                    if total_money >= 3.0:
                        change_req = total_money - 3.0
                        print(f'change returned is {change_req}')
                    else:
                        print('The money is insufficient so Money refunded')

                elif asking == 'latte':
                    if total_money >= 2.5:
                        change_req = total_money - 2.5
                        print(f'change returned is {change_req}')
                    else:
                        print('The money is insufficient so Money refunded')
                make_coffee()
            else:
                print('Sorry we dont have enough resources')
while input('Do you want the assistance of our coffee machine for any query'
            'press y for yes and n for no :\n').lower()=='y':
    os.system('cls')
    start()