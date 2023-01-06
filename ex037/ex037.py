#  Ex037 - Write a Python program that reads any integer and asks
# the user to choose the conversion base: 1 for binary,
# 2 for octal and 3 for hexadecimal.

integer = int(input('Enter an integer: '))
print('Choose one of the bases for conversion:')
print('[1] Convert to BINARY')
print('[2] Convert to OCTAL')
print('[3] Convert to HEXADECIMAL')
choice = int(input('Choice: '))

if choice == 1:
    print(f'{integer} converted to BINARY equals {bin(integer)[2:]}')
elif choice == 2:
    print(f'{integer} converted to OCTAL equals {oct(integer)[2:]}')
elif choice == 3:
    print(f'{integer} converted to HEXADECIMAL equals {hex(integer)[2:]}')
else:
    print('Invalid option. Try again.')
