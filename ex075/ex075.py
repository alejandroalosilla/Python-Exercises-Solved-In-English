#  Ex075 - Develop a program that reads four values from the keyboard and
# stores them in a tuple.
#  At the end, show:
# A) How many times did the value 9 appear.
# B) In which position was entered the first value 3.
# C) What were the even numbers.

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
n4 = int(input('Enter the fourth number: '))

numbers = (n1, n2, n3, n4)

print(f'The value 9 appeared {numbers.count(9)} times')
print(f'The value 3 appeared in the {numbers.index(3) + 1}º position.')
print('The even values entered were ', end='')

for number in range(0, len(numbers)):
    if numbers[number] % 2 == 0:
        print(f'{numbers[number]}', end=' ')
