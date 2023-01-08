#  Ex058 - Improve the game of CHALLENGE 028 where the computer will
# "think" of a number between 0 and 10.
#  But now the player will try to guess until he gets it right,
# showing in the end how many guesses were needed to win.

from random import randint

pc_number = randint(1, 10)
player_number = 0
number_tries = 0

print('I am your computer...')
print('I thought of a number between 1 and 10.')
print('Can you guess which one it was?')

while pc_number != player_number:
    player_number = int(input('What is your guess? '))
    if pc_number > player_number:
        print('More... try one more time.')
    elif pc_number < player_number:
        print('Less... try one more time.')
    number_tries += 1
print(f'You got it right with {number_tries} tries. Congratulations!')
