#  Ex039 - Make a program that reads the year of birth of a young person
# and informs, according to his age, if he is still going to
# enlist in the military service, if it is the exact time to enlist
# or if it is past the enlistment time.
#  Your program should also show the time left or overdue.

from datetime import datetime

current_year = datetime.now().year
birth_year = int(input('Year of birth: '))
age = current_year - birth_year

if age < 18:
    print(f'Those born in {birth_year} are {age} years old in {current_year}.')
    print(f'There are still {18 - age} years left for military enlistment.')
    print(f'Your enlistment will be in {current_year + (18 - age)}.')
elif age == 18:
    print(f'Those born in {birth_year} are {age} years old in {current_year}.')
    print('You must enlist IMMEDIATELY.')
else:
    print(f'Those born in {birth_year} are {age} years old in {current_year}.')
    print(f'You should have enlisted {age - 18} years ago.')
    print(f'Your enlistment was on {current_year - (age - 18)}.')
