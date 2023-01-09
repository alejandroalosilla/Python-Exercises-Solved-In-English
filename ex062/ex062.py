#  Ex062 - Improve CHALLENGE 061 by asking the user if he wants to show
# some more terms.
#  The program will exit when it says it wants to show 0 terms.

print('AP generator')
print(10 * '-=')
first_term = int(input('First term: '))
ratio = int(input('Ratio: '))

c = 1
number_of_terms = 10

while c < 11:
    print(f'{first_term} -> ', end='')
    first_term += ratio
    c += 1
    if c == 11:
        print('Pause')
        more_terms = int(input('How many terms do you want to show more? '))
        if more_terms == 0:
            c = 12
        else:
            c -= more_terms
            number_of_terms += more_terms
print(f'Progression finished with {number_of_terms} terms shown.')
