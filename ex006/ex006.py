#  Ex006 - Create an algorithm that reads a number and outputs
# its double, triple, and square root.

from math import sqrt

number = int(input('Enter a number: '))

double = number * 2
triple = number * 3
square_root = sqrt(number)

print(f'The double of {number} equals {double}.')
print(f'The triple of {number} is equal to {triple}.')
print(f'The square root of {number} is equal to {square_root:.2f}.')
