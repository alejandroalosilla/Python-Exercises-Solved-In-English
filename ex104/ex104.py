#  Ex104 - Create a program that has the readint() function, which will work
# similarly to Python's input() function, only doing the validation to
# accept only a numeric value.
# Ex: n = readInt('Type an n: ')


def readint(n):
    n = str(input(n))
    while n == '' or n.isalpha():
        print(f'\033[31mERROR! Please enter a valid integer!\033[m')
        n = str(input('Enter a number: '))
    return n


print(30 * '-')
number = readint('Enter a number: ')
print(f'\033[32mYou just entered the number {number}')
