#  Ex017 - Write a program that reads the length of the opposite
# and adjacent sides of a right triangle.
# Calculate and show the length of the hypotenuse.

from math import sqrt

op_side = float(input('Length of the opposite side: '))
ad_side = float(input('length of the adjacent side: '))

hypotenuse = sqrt(pow(op_side, 2) + (pow(ad_side, 2)))

print(f'The hypotenuse will measure {hypotenuse:.2f}')
