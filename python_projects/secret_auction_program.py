import os
print("******{Welcome to silent auction program}*******")
flag=True
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def print_stake_holder(dict1):
    max=-1
    name=""
    for i in dict1:
        if(max<dict1[i]):
            max=dict1[i]
            name=i
    print(f"the winner is {name} with {max} amount")
print(f'{logo}\nWelcome to the secret aution program')
while flag:
    name = input("Enter the name of participant : ")
    dict1 = {}
    prize = int(input("enter ur bidding prize :"))
    dict1[name] = prize
    ask = input("is there any other bidders :")
    if ask == 'yes':
        os.system('cls')
    elif ask=='no':
        flag=False
        print_stake_holder(dict1)


