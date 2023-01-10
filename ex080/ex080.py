#  Ex080 - Create a program where the user can enter five numerical values
# and register them in a list, already in the correct insertion
# position (without using sort()).
#  At the end, show the sorted list on the screen.

numbers_list = list()
for c in range(0, 5):
    number = int(input("Enter a number: "))
    if c == 0 or number > numbers_list[-1]:
        numbers_list.append(number)
    else:
        for pos, x in enumerate(numbers_list):
            if number <= x:
                numbers_list.insert(pos, number)
                break
print(30 * '-=')
print(f'The values entered in order were {numbers_list}')
