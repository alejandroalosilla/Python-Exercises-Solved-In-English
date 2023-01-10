#  Ex071 - Create a program that simulates the operation of an electronic box.
#  At first, ask the user what will be the amount to be withdrawn
# (integer number) and the program will inform how many bills of
# each value will be delivered.
#  Consider that the box has banknotes of $50, $20, $10 and $1.

print(20 * '=')
print('     TEST BANK')
print(20 * '=')

value = int(input('What amount do you want to withdraw? $'))
banknote = 50

while True:
    if (value // banknote) > 0:
        print(f'Total of {value // banknote} banknotes of {banknote}')
    value = value % banknote
    if value == 0:
        break

    if banknote == 50:
        banknote = 20
    elif banknote == 20:
        banknote = 10
    elif banknote == 10:
        banknote = 1

print(20 * '=')
print('End of program!')
