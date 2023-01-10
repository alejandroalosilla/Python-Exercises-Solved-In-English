#  Ex074 - Create a program that will generate five random numbers and put
# them in a tuple.
#  After that, show the list of generated numbers and also indicate
# the smallest and largest values that are in the tuple.

from random import randint

random_numbers = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print(f'The values drawn were: ', end='')
for n in range(0, len(random_numbers)):
    print(random_numbers[n], end=' ')

print(f'\nThe highest value drawn was {max(random_numbers)}')
print(f'The lowest value drawn was {min(random_numbers)}')
