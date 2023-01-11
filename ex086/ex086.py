#  Ex086 - Create a program that declares a 3x3 dimension matrix and fills it
# with values read from the keyboard.
#  In the end, show the matrix on the screen, with the correct
# formatting.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Enter a value for [{row}, {column}]: '))
print(30 * '-=')
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end='')
    print()
    