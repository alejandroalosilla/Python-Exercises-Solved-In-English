# Ex029 - Write a program that reads the speed of a car.
# If he exceeds 80 km/h, show a message saying he was fined.
# The fine will cost $7.00 for each km over the limit.

# colors:
yellow = '\033[33m'
green = '\033[32m'
red = '\033[31m'
close = '\033[m'

car_speed = float(input('What is the current speed of the car? '))

if car_speed <= 80:
    print(f'{yellow}Have a nice day! Drive safely!')
else:
    print(f'{red}FINED! You have exceeded the permitted speed limit of 80 km/h.')
    print(f'You must pay a fine of {green}${7 * (car_speed - 80):.2f}!')
    print(f'{yellow}Have a nice day! Drive safely!')
