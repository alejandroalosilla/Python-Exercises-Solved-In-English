#  Ex060 - Write a program that reads any number
# and displays its factorial.
#  Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

number = int(input('Enter a number to\ncalculate your factorial: '))
m = number
print('Calculating 6! = ', end='')
while number > 1:
    print(f'{number} X ', end='')
    number -= 1
    if number == 1:
        print('1 = ', end='')
    m *= number
print(m)
