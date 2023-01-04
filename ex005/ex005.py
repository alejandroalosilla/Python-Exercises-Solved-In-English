#  Ex005 - Write a program that reads an Integer number and displays
# its successor and predecessor on the screen.

number = int(input('Enter a number: '))

successor = number + 1
predecessor = number - 1

print(f'Analyzing the value {number}, its predecessor is'
      f' {predecessor} and the successor is {successor}.')
