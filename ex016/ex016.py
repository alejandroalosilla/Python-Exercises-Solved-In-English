#  Ex016 - Create a program that reads any Real number from the keyboard
# and displays its Integer portion on the screen.

from math import trunc

real_number = float(input('Enter a value: '))
print(f'The value entered was {real_number} and its integer portion is {trunc(real_number)}.')
