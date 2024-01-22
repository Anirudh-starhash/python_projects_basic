#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
import os


def play_game():
    print(logo)
    print('Welcome to number gussing game')
    asking = input(
        'Choose a dificulty type \'easy\' for easy and \'hard\' for hard\n')

    if asking == 'hard':
        guess = 5
    else:
        guess = 10

    number = random.randint(1, 100)

    is_gameover = False

    while not is_gameover:
        num = int(input('choose a number between 1 and 100\n'))
        print(f"you have {guess} attempts left")

        if (num > number):
            guess -= 1
            print('Too high')
        elif num < number:
            guess -= 1
            print('Too low')
        else:
            print('You win')
            is_gameover = True

        print(f'Try again you have {guess} attempts left')
        if guess == 0:
            is_gameover = True
            print(f'You lose and the right number is {number}')


while input(
        'Do you want the play the number guessing game type y for yes and n for no\n'
) == 'y':
    os.system('cls')
    play_game()
