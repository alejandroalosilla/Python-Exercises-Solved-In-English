#  Ex023 - Write a program that reads a number from 0 to 9999 and displays
# each of the digits separately.

number = int(input('Enter a number: '))

thousands = number // 1000
number = number % 1000
hundreds = number // 100
number = number % 100
dozens = number // 10
units = number % 10

print(f'thousands: {thousands}')
print(f'hundreds: {hundreds}')
print(f'dozens: {dozens}')
print(f'units: {units}')
