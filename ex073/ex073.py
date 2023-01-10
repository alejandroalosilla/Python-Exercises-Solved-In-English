#  Ex073 - Create a tuple filled with the top 5 NBA rankings, in ranking order.
#  Then show:
# a) The top 3 teams.
# b) The last 2 placed in the ranking.
# c) Teams in alphabetical order.
# d) What ranking is the Cleveland Cavaliers basketball team in.

teams = ('Boston Celtics', 'Milwaukee Bucks', 'Cleveland Cavaliers',
         'Atlanta Hawks', 'Indiana Pacers')

print(30 * '-=')
print(f'Basketball teams: {teams}')
print(30 * '-=')
print(f'The top 3 are: {teams[0:3]}')
print(30 * '-=')
print(f'The last 2 are: {teams[3:]}')
print(30 * '-=')
print(f'Teams in alphabetical order: {sorted(teams)}')
print(30 * '-=')
print(f"The Cleveland Cavaliers team is in {teams.index('Cleveland Cavaliers') + 1}º position.")
