#  Ex041 - The National Swimming Confederation needs a program that reads
# the year of birth of an athlete and shows their category,
# according to age:
# - Up to 14 years old: CHILDREN
# - Up to 19 years old: JUNIOR
# - Up to 25 years old: SENIOR
# - Above 25 years: MASTER

from datetime import datetime

birth_year = int(input('Year of birth: '))
current_year = datetime.now().year
age = current_year - birth_year

if age < 14:
    print(f'The athlete is {age} years old.')
    print('Category: CHILDREN')
elif 14 < age <= 19:
    print(f'The athlete is {age} years old.')
    print('Category: JUNIOR')
elif 19 < age <= 25:
    print(f'The athlete is {age} years old.')
    print('Category: SENIOR')
else:
    print(f'The athlete is {age} years old.')
    print('Category: MASTER')
