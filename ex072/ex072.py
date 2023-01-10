#  Ex072 - Create a program that has a fully populated tuple with a count
# spelled out from zero to twenty.
#  Your program should read a number from the keyboard (between 0 and
# 20) and display it in full.

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six',
           'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen',
           'seventeen', 'eighteen', 'nineteen', 'twenty')

number = int(input('Enter a number between 0 and 20: '))

while True:
    if number < 0 or number > 20:
        number = int(input('Try again. Enter a number between 0 and 20: '))
    else:
        break
print(f'You entered the number {numbers[number]}')
