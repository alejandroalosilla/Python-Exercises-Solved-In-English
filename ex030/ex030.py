#  Ex030 - Create a program that reads an integer and shows on the screen
# whether it is EVEN or ODD.

# color:
blue = '\033[34m'
purple = '\033[35m'

number = int(input('Tell me any number: '))

if number % 2 == 0:
    print(f'Number {number} is {blue}EVEN')
else:
    print(f'Number {number} is {purple}ODD')
