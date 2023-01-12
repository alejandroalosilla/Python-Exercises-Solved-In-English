#  Ex094 - Create a program that reads the name, gender and age of several
# people, storing each person's data in a dictionary and all dictionaries
# in a list.
#  At the end, show:
# A) How many people were registered
# B) The average age
# C) A list of women
# D) A list of people above average age

temporary_data = dict()
people_list = list()
women_list = list()
sum_of_ages = 0

while True:
    temporary_data['Name'] = str(input('Name: ')).strip().capitalize()
    while True:
        temporary_data['Gender'] = str(input('Gender [M/F]: ')).strip().upper()
        if temporary_data['Gender'] in 'MF':
            break
        else:
            print(f'\033[31mERROR! Please only type M or F!\033[m')

    if temporary_data['Gender'] == 'F':
        women_list.append(temporary_data['Name'])

    temporary_data['Age'] = int(input('Age: '))
    sum_of_ages += temporary_data['Age']

    people_list.append(temporary_data.copy())
    temporary_data.clear()

    while True:
        option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
        if option in 'YN':
            break
        else:
            print('\033[31mERROR! Answer only Y or N.\033[m')
    if option == 'N':
        break
print(30 * '-=')
print(f'A) In all we have {len(people_list)} people registered.')
print(f'B) The average age is {sum_of_ages / len(people_list):.2f} years.')
print(f'C) The registered women were: ', end='')
for c in women_list:
    print(f'[{c}] ', end='')
print()
print(f'D) List of people above average age:')

for p in people_list:
    if p['Age'] > (sum_of_ages / len(people_list)):
        for k, v in p.items():
            print(f'   {k} = {v};', end='')
        print()
print('<< END >>')
