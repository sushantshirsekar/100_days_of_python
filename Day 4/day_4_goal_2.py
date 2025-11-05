# =================================================================================
# Script Name   : Rock, Paper, Scissors Game
# Script Purpose: A simple console-based Rock, Paper, Scissors game
#                 implemented using lists, randomization, and conditional logic.
#                 The player competes against the computer, and the winner
#                 is decided based on standard game rules.
# =================================================================================


from random import random, randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_inp = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_inp = randint(0, 2)
game_arr = [rock, paper, scissors]
if user_inp > 2 or user_inp < 0:
    print('Invalid Input you loose')
else:
    print('You Choose:\n')
    print(game_arr[user_inp] + '\n')
    print('Computer Choose:\n')
    print(game_arr[computer_inp] + '\n')
    if user_inp == computer_inp:
        print('''It's a Tie''')
    elif user_inp == 0:
        if computer_inp == 2:
            print('You Win!')
        else:
            print('Computer Wins!')
    elif user_inp == 1:
        if computer_inp == 0:
            print('You Win!')
        else:
            print('Computer Wins!')
    elif user_inp == 2:
        if computer_inp == 1:
            print('You Win!')
        else:
            print('Computer Wins!')
