#  Ex068 - Write a program that plays even or odd with the computer.
#  The game will only stop when the player loses, showing the
# total number of consecutive wins he has achieved at the end
# of the game.

from random import randint

pc_choice = randint(1, 10)
number_of_wins = 0

print(20 * '=-')
print('LET IS PLAY ODD OR EVEN')
print(20 * '=-')

while True:
    player_value = int(input('Enter a value [1-10]: '))
    even_or_odd = str(input('Even or Odd? [E/O]: ')).strip().upper()[0]
    pc_value = randint(1, 10)

    if even_or_odd == 'E':
        if (player_value + pc_value) % 2 == 0:
            print(60 * '-')
            print(f'You played {player_value} and the computer {pc_value}. Total {player_value + pc_value} -> EVEN')
            print(60 * '-')
            print('You won!')
            print('Let is play again...')
            print(20 * '=-')
            number_of_wins += 1
        else:
            print(60 * '-')
            print(f'You played {player_value} and the computer {pc_value}. Total {player_value + pc_value} -> ODD')
            print(60 * '-')
            break
    elif even_or_odd == 'O':
        if (player_value + pc_value) % 2 == 0:
            print(60 * '-')
            print(f'You played {player_value} and the computer {pc_value}. Total {player_value + pc_value} -> EVEN')
            print(60 * '-')
            break
        else:
            print(60 * '-')
            print(f'You played {player_value} and the computer {pc_value}. Total {player_value + pc_value} -> ODD')
            print(60 * '-')
            print('You won!')
            print('Let is play again...')
            print(20 * '=-')
            number_of_wins += 1
print(f'GAME OVER! You won {number_of_wins} times.')
