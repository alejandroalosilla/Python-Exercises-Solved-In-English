# Ex027 - Write a program that reads a person's full name, then displays the first and last name separately.
# Ex: Ana Maria de Souza (first = Ana; last = Souza.)

name = str(input('Enter your full name: ')).strip().split()
last_name = len(name)

print('Very nice to meet you!')
print(f'Your first name is {name[0]}')
print(f'Your last name is {name[last_name - 1]}')
