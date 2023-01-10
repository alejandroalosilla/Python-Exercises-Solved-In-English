#  Ex078 - Write a program that reads 5 numerical values and stores them in a
# list.
#  At the end, show which was the largest and smallest value typed and
# their respective positions in the list.

numbers_list = list()

for counter in range(0, 5):
    numbers_list.append(int(input(f'Enter a value for position {counter}: ')))

print(30 * '-=')
print(f'You entered the values: {numbers_list}')
print(f'The highest value entered was {max(numbers_list)} in the positions ', end='')
for position, value in enumerate(numbers_list):
    if value == max(numbers_list):
        print(f'{position}...', end=' ')
print(f'\nThe smallest value entered was {min(numbers_list)} in the positions ', end='')
for position, value in enumerate(numbers_list):
    if value == min(numbers_list):
        print(f'{position}...', end=' ')
