import random
import os
from hangman_words import word_list
flag=True
while flag:
    # word_list = ['anirudh', 'sandilya', 'manideep', 'eeswar', 'saikartik', 'anshu', 'soham',
    #              'rashwin','merugupavankalyan','chaitanya','sravan','chinnarayudu']
    print("Hey let's play the Hangman game.....")
    print("Guess the word as shown below to fill the blank places u have 6 attempts...")
    print("If u loose ur 6 lives ur dead bro....")
    list = []
    word=random.choice(word_list)
    for i in word: list.append("_")
    print(list)
    def list_filled(list1):
        count = 0
        for i in range(len(list)):
            if (list[i] == '_'): return True
        return False
    def find_pos(word, char, list):
        store = []
        for i in range(len(word)):
            if char == word[i]:
                store.append(i)
        for j in range(len(store)):
            list[store[j]] = char
    def Hangman_print(Hangman):
        for i in range(len(Hangman)):
            size = ""
            for j in range(len(Hangman[i])):
                size += Hangman[i][j]
            print(size)
    attempt = 6
    Hangman = [['-', '-', '-', '-', '-', '='], [' ', ' ', '|', ' ', ' ', '='], [' ', ' ', ' ', ' ', ' ', '='],
               [' ', ' ', ' ', ' ', ' ', '=']
        , [' ', ' ', ' ', ' ', ' ', '=']]
    Hangman_print(Hangman)
    while (list_filled(list) and attempt):
        char = input("Guess the letter : ")
        if (word.count(char) == 0):
            attempt -= 1
            if attempt == 5: Hangman[2][2] = '0'
            elif attempt == 4: Hangman[3][2] = '|'
            elif attempt == 3: Hangman[3][1] = '/'
            elif attempt == 2: Hangman[3][3] = '\\'
            elif attempt == 1: Hangman[4][1] = '/'
            else: Hangman[4][3] = '\\'
        else:
            find_pos(word, char, list)
            print(list)
        Hangman_print(Hangman)
        print(f"You have {attempt} lives left still use them properly")
    if (list_filled(list)):
        print("You lose ")
        print(f"Actual word is {word}")
    else:
        print(f"You won and you have {attempt} lives left")
    guess = int(input("Do u want to play this game one more time enter 1 for yes and 0 for no ? :"))
    if (guess == 0): flag = False
    else:
        os.system('cls')
