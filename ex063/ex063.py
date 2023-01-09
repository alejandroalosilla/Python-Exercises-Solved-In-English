#  Ex063 - Write a program that reads any integer N and displays the
# first N elements of a Fibonacci Sequence on the screen.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print(20 * '-')
print('Fibonacci Sequence')
print(20 * '-')
number_of_terms = int(input('How many terms do you want to show? '))
counter = 0
first_term = 0
second_term = 1
third_term = first_term + second_term
print(30 * '-')
print(f'{first_term} -> {second_term} -> ', end='')
while counter < number_of_terms - 2:
    print(f'{third_term} -> ', end='')
    first_term = second_term
    second_term = third_term
    third_term = first_term + second_term
    counter += 1
print('End')
print(30 * '-')
