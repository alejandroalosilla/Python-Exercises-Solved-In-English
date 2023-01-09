#  Ex066 - Create a program that reads integers from the keyboard.
#  The program will only stop when the user types the value 999,
# which is the stop condition.
#  At the end, show how many numbers were entered and what was
# the sum between them (disregarding the flag).

numbers_counter = 0
numbers_sum = 0

while True:
    value = int(input('Enter a value (999 to stop): '))
    if value == 999:
        break
    else:
        numbers_counter += 1
        numbers_sum += value
print(f'The sum of the {numbers_counter} values was {numbers_sum}!')
