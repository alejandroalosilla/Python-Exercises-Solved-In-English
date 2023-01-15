#  Ex101 - Create a program that has a function called vote() that will receive a person's year of birth
# as a parameter, returning a literal value indicating whether a person has a DENIED vote or an
# OPTIONAL vote in elections.

from datetime import datetime

cy = datetime.now().year


def vote(y):
    a = cy - y
    if a >= 18:
        print(f'-> {a} years old: OPTIONAL VOTE!')
    else:
        print(f'-> {a} years old: CANNOT VOTE!')


print(30 * '-')
yb = int(input('What year were you born? '))
vote(yb)
