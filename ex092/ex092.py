#  Ex092 - Write a program that reads a person's name, year of birth, and driver's license number
# into a dictionary.
#  If the driver's license number is different from ZERO, the dictionary will also receive the
# year of issue of the driver's license.
#  Calculate how old the person will be when they renew their driver's license.
#  -> Validity of the driver's license equal to 8 years.

from datetime import datetime

current_year = datetime.now().year

person = dict()

person['Name'] = str(input('Name: ')).strip().capitalize()
person['Age'] = abs(int(input('Year of birth: ')) - current_year)
person['Driver License'] = int(input("Driver's license number: "))

if person['Driver License'] != 0:
    person["Driver's license year"] = int(input("Driver's license year: "))
    person['Age in the future'] = 8 - (current_year - person["Driver's license year"]) + person['Age']
print(30 * '-=')
for k, v in person.items():
    print(f'{k} equals {v}')
