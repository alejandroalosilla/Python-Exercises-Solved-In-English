#  Ex048 - Write a program that calculates the sum of all odd numbers
# that are multiples of 3 and are in the range 1 to 500.

s = 0
t = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        t += 1
print(f'The sum of all {t} requested values is {s}')
