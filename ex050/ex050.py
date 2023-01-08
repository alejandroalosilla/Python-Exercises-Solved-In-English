#  Ex050 - Develop a program that reads six integers and prints the sum
# of only those that are even. If the entered value is odd,
# disregard it.

odd_sum = 0
total_odd_numbers = 0

for c in range(1, 7):
    number = int(input(f'Enter the {c}º value: '))
    if number % 2 == 0:
        odd_sum += number
        total_odd_numbers += 1
print(f'You entered {total_odd_numbers} even numbers and the sum was {odd_sum}')
