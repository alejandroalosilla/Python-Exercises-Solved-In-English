#  Ex031 - Develop a program that asks for the distance of a trip in Km.
# Calculate the ticket price, charging $0.50 per km for trips
# of up to 200 km and $0.45 for longer trips.

far = float(input('How far is your trip? '))

if far <= 200:
    price = far * 0.5
else:
    price = far * 0.45

print(f'You are about to start a {far:.2f}km journey.')
print(f'And the price of your ticket will be ${price:.2f}')
