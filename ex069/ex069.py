#  Ex069 - Create a program that reads the age and gender of multiple people.
# For each person registered, the program should ask if the user wants
# to continue or not.
#  At the end, show:
# A) How many people are over 18 years old.
# B) how many men were registered.
# C) how many women are under 20 years old.

total_over_18 = 0
men_counter = 0
woman_under_20 = 0
option = ''

while True:
    print(30 * '-')
    print('     REGISTER A PERSON')
    print(30 * '-')

    age = int(input('Age: '))
    gender = str(input('gender [M/F]: ')).strip().upper()[0]
    option = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]

    if age > 18:
        total_over_18 += 1
    if gender == 'M':
        men_counter += 1
    if age < 20 and gender == 'F':
        woman_under_20 += 1
    if option == 'N':
        break

print(f'Total people over 18 years old: {total_over_18}')
print(f'In all we have {men_counter} registered men')
print(f'And we have {woman_under_20} women under 20 years old')
