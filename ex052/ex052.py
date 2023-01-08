#  Ex052 - Write a program that reads an integer and tells whether
#  it is a prime number.

divisible_times = 0
number = int(input('Enter a number: '))

for c in range(1, number + 1):
    if number % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        divisible_times += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if divisible_times > 2:
    print(f'\nThe number {number} was divisible {divisible_times} times.')
    print('And therefore the number is not prime.')
else:
    print(f'\nThe number {number} was divisible {divisible_times} times.')
    print('And so the number is prime.')
