#  Ex084 - Make a program that reads name and weight of several people,
# keeping everything in a list.
#  At the end, show:
# A) How many people were registered.
# B) A list of the heaviest people.
# C) A list of the lightest people.

main_list = list()
temporary_list = list()
greater = 0
less = 0
counter = 0

while True:
    temporary_list.append(str(input('Name: ')).strip())
    temporary_list.append(float(input('Weight: ')))
    if len(main_list) == 0:
        greater = temporary_list[1]
        less = temporary_list[1]
    if temporary_list[1] > greater:
        greater = temporary_list[1]
    if temporary_list[1] < less:
        less = temporary_list[1]

    main_list.append(temporary_list[:])
    temporary_list.clear()
    counter += 1

    option = ''
    while option != 'Y' and option != 'N':
        option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if option == 'N':
        break

print(30 * '-=')
print(f'In all, you registered {counter} people.')
print(f'The highest weight was {greater:.2f}Kg. Weight of ', end='')
for c in range(0, len(main_list)):
    if main_list[c][1] == greater:
        print(f'[{main_list[c][0]}]', end=' ')
print(f'\nThe smallest weight was {less:.2f}kg. Weight of ', end='')
for c in range(0, len(main_list)):
    if main_list[c][1] == less:
        print(f'[{main_list[c][0]}]', end=' ')
