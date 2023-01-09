#  Ex065 - Create a program that reads several integers from the keyboard.
#  At the end of the run, show the mean of all values and which was
# the highest and lowest values read.
#  The program should ask the user whether he wants to continue
# typing values.
option = 'Y'
highest_value = 0
lowest_value = 0
counter = 0
number_sum = 0

while option == 'Y':
    number = int(input('Enter a number: '))
    option = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if counter == 0:
        lowest_value = number
    if number > highest_value:
        highest_value = number
    if number < lowest_value:
        lowest_value = number
    counter += 1
    number_sum += number
print(f'You entered {counter} numbers and the average was {(number_sum / counter):.2f}')
print(f'The highest value was {highest_value} and the lowest was {lowest_value}')
