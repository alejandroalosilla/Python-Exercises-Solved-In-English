# Ex038 - Write a program that reads two integers and compares them.
# showing a message on the screen:
# - The first value is greater
# - The second value is greater
# - There is no greater value, both are equal

first_number = int(input('First number: '))
second_number = int(input('Second number:'))

if first_number > second_number:
    print('The FIRST value is greater')
elif first_number < second_number:
    print('The SECOND value is greater')
else:
    print('Both values are EQUAL')
