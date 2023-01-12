#  Ex093 - Create a program that manages the performance of a football player.
#  The program will read the player's name and how many games he played.
#  Then you will read the number of goals scored in each match.
#  In the end, all of this will be stored in a dictionary, including
# the total number of goals scored during the championship.

goals_list = list()
players = dict()

players['Name'] = str(input("Player's name: ")).strip().capitalize()
plays = int(input(f"How many games did {players['Name']} play? "))

for c in range(0, plays):
    goals_list.append(int(input(f'How many goals in match {c}? ')))
players['Plays'] = goals_list
players['Total goals'] = sum(goals_list)
print(30 * '-=')

for k, v in players.items():
    print(f'{k} has the value {v}.')
print(30 * '-=')
print(f"The player {players['Name']} played {len(goals_list)} games.")
for position, v in enumerate(goals_list):
    print(f'   => In match {position}, he scored {v} goals.')
print(f'It was a total of {sum(goals_list)} goals.')
