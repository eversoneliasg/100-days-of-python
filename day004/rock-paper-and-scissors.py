# Rock, Paper and Scissors Game

import random

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
plays = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
print(plays[player_choice])
print("Computer choose:")
computer_choice = random.randint(0, 2)
print(plays[computer_choice])

if player_choice == 0:
    if computer_choice == 0:
        print("Draw!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("Draw!")
    else:
        print("You lose!")
else:
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("Draw!")
