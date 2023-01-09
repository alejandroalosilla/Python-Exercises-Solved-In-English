#  Ex067 - Write a program that displays the table of several numbers,
# one at a time, for each value entered by the user.
#  The program will stop when the requested number is negative.

while True:
    value = int(input('Do you want to see the table of what value? '))
    if value < 0:
        break
    else:
        print(30 * '-')
        for c in range(1, 11):
            print(f'{value} X {c:2} = {value * c}')
        print(30 * '-')
print('End of program!')
