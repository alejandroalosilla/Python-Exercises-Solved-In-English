#  Ex064 - Create a program that reads several integers from the keyboard.
#  The program will only stop when the user types the value 999, which
# is the stop condition.
#  At the end, show how many numbers were entered and what was
# the sum between them (disregarding the flag).

number = 0
numbers_sum = 0
total_numbers = 0
while number != 999:
    number = int(input('Enter a number [999 to stop]: '))
    if number != 999:
        total_numbers += 1
        numbers_sum += number
print(f'You entered {total_numbers} numbers and the sum between them was {numbers_sum}.')
