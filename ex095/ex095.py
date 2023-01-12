#  Ex095 - Improve the 93 challenge to work with multiple players, including
# a detailed view of each player's performance.

players_list = list()
goals_list = list()
temporary_data = dict()

while True:
    temporary_data['Name'] = str(input("Player's name: ")).strip().capitalize()
    number_of_matches = int(input(f"How many matches has {temporary_data['Name']} played? "))

    for counter in range(1, number_of_matches + 1):
        goals_list.append(int(input(f'How many goals in match {counter}? ')))
    temporary_data['Matches'] = goals_list.copy()
    temporary_data['Total Goals'] = sum(goals_list.copy())
    players_list.append(temporary_data.copy())
    temporary_data.clear()
    goals_list.clear()

    while True:
        option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
        if option in 'YN':
            break
        else:
            print('\033[31mERROR! Answer only Y or N.\033[m')

    if option == 'N':
        break
print(30 * '-=')
print('Code Name         Goals              Total')
print(43 * '-')

for position, player in enumerate(players_list):
    print(f"{position:>4} {player['Name']:<13}{str(player['Matches']):<15}{player['Total Goals']:>7}")
print(43 * '-')

while True:
    player_code = int(input('Show data of which player? '))

    if player_code == 999:
        break

    while player_code > len(players_list) - 1 and player_code != 999:
        print(f'\033[31mERROR! There is no player with code {player_code}\033[m')
        player_code = int(input('Show data of which player? '))

    if player_code == 999:
        break

    print(f" -- Performance of the player {players_list[player_code]['Name']}:")
    for position, value in enumerate(players_list[player_code]['Matches']):
        print(f'    In game {position + 1} he scored {value} goals.')
print('<< END OF PROGRAM... >>')
