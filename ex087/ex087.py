#  Ex087 - Improve the previous challenge, showing at the end:
# A) The sum of all even values entered.
# B) The sum of the values in the third column.
# C) The largest value in the second row.

even_sum = 0
third_column = 0

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Enter a value for [{row}, {column}]: '))
        if matrix[row][column] % 2 == 0:
            even_sum += matrix[row][column]
        if column == 2:
            third_column += matrix[row][column]

print(30 * '-=')
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end='')
    print()
print(30 * '-=')
print(f'The sum of the even values is {even_sum}')
print(f'The sum of the values in the third column is {third_column}')
print(f'The highest value in the second row is {max(matrix[1])}')
