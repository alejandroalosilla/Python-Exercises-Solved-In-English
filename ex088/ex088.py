#  Ex088 - Make a program that helps a jackpot player to create guesses.
#  The program will ask how many games will be generated and will
# draw 5 numbers between 1 and 70 for each game, registering everything
# in a composite list.

from random import randint
from time import sleep

lj = list()
v = 0

print(30 * '-')
print('           JACKPOT')
print(30 * '-')

n = int(input('How many games do you want me to draw? '))
print(3 * '-=', f'DRAWING {n} GAMES', 3 * '-=')
for c in range(1, n + 1):
    for n in range(0, 6):
        while True:
            v = randint(1, 70)
            if v not in lj:
                lj.append(v)
                break
    print(f'Game {c}: {sorted(lj)}')
    lj.clear()
    sleep(1)
print(5 * '-=', 'GOOD LUCK', 5 * '-=')
