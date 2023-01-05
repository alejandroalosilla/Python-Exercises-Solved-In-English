#  Ex028 - Write a program that makes the computer "think" of an integer
# between 0 and 5 and ask the user to try to figure out which number
# was chosen by the computer. The program should write on the screen
# if the user won or lost.

from time import sleep
from random import randint

# colors:
purple = '\033[35m'
blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
close = '\033[m'

print(30 * f'{yellow}-=')
print(f'{blue}I will think of a number between 0 and 5. Try to guess...')
print(30 * f'{yellow}-={close}')

pc_number = randint(0, 5)
chosen_number = int(input('What number did I think of? '))

if pc_number == chosen_number:
    print(f'{purple}Processing...{close}')
    sleep(1)
    print(f'{green}Congratulations! You won!')
else:
    print(f'{purple}Processing...{close}')
    sleep(1)
    print(f'{red}I won! I thought of number {pc_number} not {chosen_number}!')
