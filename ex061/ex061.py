#  Ex061 - Redo CHALLENGE 051, reading the first term and the ratio
# of an AP, showing the first 10 terms of the progression
# using the while structure.

print('AP generator')
print(10 * '-=')
first_term = int(input('First term: '))
ratio = int(input('Ratio: '))

c = 1

while c < 11:
    print(f'{first_term} -> ', end='')
    first_term += ratio
    c += 1
print('End')
