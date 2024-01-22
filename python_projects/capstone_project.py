import random
import os
def playgame():
    def deal_card():
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        return random.choice(cards)
    def findsum(user_input):
        if sum(user_input)==21 and len(user_input)==2:
            return 0
        if 11 in user_input and sum(user_input)>21:
            user_input.remove(11)
            user_input.append(1)
        return sum(user_input)

    def compare(user_score,computer_ascore):
        if user_score==computer_score:
            return 'Draw'
        elif computer_score==0:
            return 'computer_won'
        elif user_score==0:
            return 'user_won'
        elif user_score>21:
            return 'computer_won'
        else:
            if(user_score>computer_score):
                return 'user_won'
            else:
                return 'computer_won'

    user_input=[]
    computer_input=[]
    is_gameover=False

    for _ in range(2):
        user_input.append(deal_card())
        computer_input.append(deal_card())
    print('Welcome to blackjack capstone project!')
    while not is_gameover:
        user_score=findsum(user_input)
        computer_score=findsum(computer_input)
        print(f"The user input cards are {user_input} and they add up to {user_score}")
        print(f"The computer's first's card is {computer_input[0]}")
        if(user_score==0 or computer_score==0 or user_score>21):
            is_gameover=True
        else:
            asking=input('do u want to get yourself revealed with the one more card type y for yes and n for no\n')
            if(asking=='n'):
                is_gameover=True
            else:
                user_input.append(deal_card())

# user's game is over now its computer's remaining game             
    while(computer_score!=0 and computer_score<17):
        computer_input.append(deal_card())
        computer_score=findsum(computer_input)
    
    print(f'your final hand has {user_input} and the final score is {user_score}')        
    print(f'the computer\'s final_hand final hand has {computer_input} and the final score is {computer_score}')
    print(compare(user_score,computer_score))

while input('do u want the blackjack game\n')=='y':
    os.system('cls')
    playgame()
        
    

    