#  Ex082 - Create a program that will read several numbers and put them in a
# list.
#  After that, create two extra lists that will contain only the even
# and odd values entered, respectively.
#  At the end, show the contents of the three generated lists.

numbers_list = list()
even_list = list()
odd_list = list()

while True:
    numbers_list.append(int(input('Enter a value: ')))
    option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]

    if option == 'N':
        break

print(30 * '-=')
print(f'The complete list is {numbers_list}')
for c in range(0, len(numbers_list)):
    if numbers_list[c] % 2 == 0:
        even_list.append(numbers_list[c])
    else:
        odd_list.append(numbers_list[c])
print(f'The list of even numbers is {even_list}')
print(f'The list of odd numbers is {odd_list}')
