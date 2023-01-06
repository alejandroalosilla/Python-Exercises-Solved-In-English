#  Ex033 - Write a program that reads three numbers and shows which is
# the highest and which is the smallest.

n1 = int(input('First value: '))
n2 = int(input('Second value: '))
n3 = int(input('Third value: '))

highest = 0
smallest = 0

# highest
if n1 > n2 and n1 > n3:
    highest = n1
elif n2 > n1 and n2 > n3:
    highest = n2
elif n3 > n1 and n3 > n2:
    highest = n3

# smallest
if n1 < n2 and n1 < n3:
    smallest = n1
elif n2 < n1 and n2 < n3:
    smallest = n2
elif n3 < n1 and n3 < n2:
    smallest = n3

print(f'The highest value entered was {highest}')
print(f'The smallest value entered was {smallest}')
