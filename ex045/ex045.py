#  Ex045 - Create a program that makes the computer play Jokenpo
# with you.

from random import randint

lis = ('Rock', 'Paper', 'Scissors')  # list
pc_choice = randint(0, 2)

print('Your options: ')
print('[0] ROCK')
print('[1] PAPER')
print('[2] SCISSORS')
move = int(input('What is your move? '))

print('JO\nKEN\nPO!!!')
print(20 * '-=')
print(f'Computer chose {lis[pc_choice]}')
print(f'Player chose {lis[move]}')
print(20 * '-=')

if pc_choice == 0:  # Computer chose Rock
    if move == 0:
        print('DRAW')
    elif move == 1:
        print('PLAYER WINS')
    elif move == 2:
        print('COMPUTER WINS')

elif pc_choice == 1:  # Computer chose Paper
    if move == 0:
        print('COMPUTER WINS')
    elif move == 1:
        print('DRAW')
    elif move == 2:
        print('PLAYER WINS')

elif pc_choice == 2:  # Computer chose Scissors
    if move == 0:
        print('PLAYER WINS')
    elif move == 1:
        print('COMPUTER WINS')
    elif move == 2:
        print('DRAW')
