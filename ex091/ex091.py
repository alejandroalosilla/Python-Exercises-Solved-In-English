#  Ex091 - Create a program where 4 players roll a die and get random results.
#  Store these results in a Python dictionary.
#  In the end, put that dictionary in order, knowing that the winner
# got the highest number on the dice.

from random import randint
from time import sleep
from operator import itemgetter
from emoji import emojize


ranking = list()

players = {'Player1': randint(1, 6),
           'Player2': randint(1, 6),
           'Player3': randint(1, 6),
           'Player4': randint(1, 6)}

for k, v in players.items():
    print(f'{k} rolls {v} on the die.')
    sleep(1)
print(players)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print(ranking)
print(30 * '-=')
print('  == RANKING ==')

for i, v in enumerate(ranking):
    if i == 0:
        print(emojize(f'   \033[32m{i+1}º place: {v[0]} with {v[1]}\033[m :1st_place_medal:'))
        sleep(1)
    elif i == 1:
        print(emojize(f'   \033[33m{i+1}° place: {v[0]} with {v[1]}\033[m :2nd_place_medal:'))
        sleep(1)
    elif i == 2:
        print(emojize(f'   \033[34m{i + 1}° place: {v[0]} with {v[1]}\033[m :3rd_place_medal:'))
        sleep(1)
    else:
        print(emojize(f'   \033[31m{i + 1}° place: {v[0]} with {v[1]}\033[m :sad_but_relieved_face:'))
        sleep(1)
