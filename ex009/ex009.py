#  Ex009 - Write a program that reads any integer number and displays
# its table on the screen.

# colors:
green = '\033[32m'
red = '\033[31m'
blue = '\033[34m'
close = '\033[m'

number = int(input('Enter a number: '))

print(20 * f'{blue}-')
print(f'{green}{number}{close} X  0 = {red}{number * 0}')
print(f'{green}{number}{close} X  1 = {red}{number * 1}')
print(f'{green}{number}{close} X  2 = {red}{number * 2}')
print(f'{green}{number}{close} X  3 = {red}{number * 3}')
print(f'{green}{number}{close} X  4 = {red}{number * 4}')
print(f'{green}{number}{close} X  5 = {red}{number * 5}')
print(f'{green}{number}{close} X  6 = {red}{number * 6}')
print(f'{green}{number}{close} X  7 = {red}{number * 7}')
print(f'{green}{number}{close} X  8 = {red}{number * 8}')
print(f'{green}{number}{close} X  9 = {red}{number * 9}')
print(f'{green}{number}{close} X 10 = {red}{number * 10}')
print(20 * f'{blue}-')
