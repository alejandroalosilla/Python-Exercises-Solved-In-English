#  Ex085 - Create a program where the user can enter seven numeric values
# and register them in a single list that keeps even and odd values
# separate.
#  At the end, show the even and odd values in ascending order.

main_list = list()
even_list = list()
odd_list = list()

for c in range(1, 8):
    value = int(input(f'Enter the {c}st value: '))
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)
main_list.append(sorted(even_list[:]))
main_list.append(sorted(odd_list[:]))

print(30 * '-=')
print(f'The even values entered were: {main_list[0]}')
print(f'The odd values entered were: {main_list[1]}')
