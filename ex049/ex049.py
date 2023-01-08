#  Ex049 - Redo CHALLENGE 009, showing the table of a number that the
# user chooses, only now using a for loop.

number = int(input('Enter a number to see your multiplication table: '))

for c in range(0, 11):
    print(f'{number} x  {c:2} = {number * c}')
