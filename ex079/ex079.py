#  Ex079 - Create a program where the user can type several numerical values
# and register them in a list.
#  If the number already exists there, it will not be added.
#  At the end, all unique values entered will be displayed, in
# ascending order.

numbers_list = list()

while True:
    value = int(input('Enter a value: '))

    if value in numbers_list:
        print('Duplicate value! I will not add...')
    else:
        numbers_list.append(value)
        print('Value added successfully...')

    option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
    if option == 'N':
        break
print(30 * '-=')
print(f'You entered the values {sorted(numbers_list)}')
