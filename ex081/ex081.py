#  Ex081 - Create a program that will read several numbers and put them in a list.
#  After that show:
# A) How many numbers were entered.
# B) The list of values, sorted in descending order.
# C) If the value 5 was typed and is or is not in the list.

numbers_list = list()
total_numbers = 0

while True:
    numbers_list.append(int(input('Enter a value: ')))
    total_numbers += 1
    option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
    if option == 'N':
        break
print(30 * '-=')
print(f'You have entered {total_numbers} elements.')
print(f'The values in descending order are {sorted(numbers_list, reverse=True)}')
if 5 in numbers_list:
    print('The value 5 is part of the list!')
else:
    print('The value 5 is not part of the list!')
