#  Ex054 - Create a program that reads the year of birth of seven people.
#  At the end, show how many people have not yet reached the age
# of majority and how many are already of age.

from datetime import datetime
current_year = datetime.now().year

adult = 0
not_adult = 0

for c in range(1, 8):
    birth_year = int(input(f'What year was the {c}º person born? '))
    age = current_year - birth_year

    if age < 18:
        not_adult += 1
    elif age >= 18:
        adult += 1
print(f'In all, we had {adult} adults')
print(f'And we also had {not_adult} underage people.')
