#  Ex057 - Write a program that reads a person's gender, but only accepts
# the values 'M' or 'F'. If it is wrong, ask for typing again until
# you have a correct value.

gender = str(input('Enter your gender [M/F]: ')).strip().upper()[0]
while gender not in 'FM':
    gender = str(input('Invalid data. Please, please inform your gender: ')).strip().upper()[0]
print(f'{gender} gender successfully registered!')
