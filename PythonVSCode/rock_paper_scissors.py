# --------------------------------------
# Using conditionals and logic operators
# ---------------------------------------

import random

computer_random = random.randint(1,3)

if computer_random =


computer_choice = 'scissors'

user_choice = input("Do you want - rock, paper, or scissors?\n")

if user_choice == computer_choice:
    print('TIE!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
else:
    print('You lose! Computer wins!')

# There is a Python Standard Library, this one includes the random lib