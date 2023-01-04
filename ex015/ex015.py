#  Ex015 - Write a program that asks for the number of kilometers traveled
# by a rented car and the number of days it was rented.
#  Calculate the price to pay, knowing that the car costs $60
# per day and $0.15 per km driven.

days = int(input('How many days rented? '))
km = float(input('How many km driven? '))

price = (days * 60) + (0.15 * km)

print(f'The total payable is ${price:.2f}.')
