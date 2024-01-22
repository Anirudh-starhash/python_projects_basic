import random
import os
from game_data import data;
from art import logo3,vs
def playgame():
    is_gameover=False
    score=0
    print(logo3)
    A=random.choice(data)
    while not is_gameover:
        B=random.choice(data)
        if(A['name']==B['name']):
            B=random.choice(data)
        print(f'Compare A: {A['name']} from {A['country']} and the description is {A['description']}')
        print(vs)
        print(f'Against B: {B['name']} from {B['country']} and the description is {B['description']}')
        asking=input('Whose has more followers: A or B\n').upper()
        if(A['follower_count']>B['follower_count']):
            ans='A'
        else:
            ans='B'
        if(asking==ans):
            score+=1
            os.system('cls')
            print(logo3)
            print(f'your correct your score is {score}')
            if ans=='B':
                A=B
        else:
            is_gameover=True
            os.system('cls')
            print(logo3)
            print(f'You are wrong your final score is {score}')
while input('Do you want to play higher or lower game type y for yes and n for no\n').lower()=='y':
    os.system('cls')
    playgame()
        