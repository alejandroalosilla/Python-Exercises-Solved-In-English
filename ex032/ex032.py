# Ex032 - Make a program that reads any year and shows if it is a leap year.

from datetime import datetime
aa = datetime.now().year

year = int(input('What year do you want to analyze? Put 0 to parse the current year: '))
if year == 0:
    year = aa

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'The year {year} IS a leap year.')
else:
    print(f'The year {year} is NOT a leap year.')
