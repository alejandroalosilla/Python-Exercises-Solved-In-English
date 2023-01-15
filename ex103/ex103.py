#  Ex103 - Write a program that has a function called data() that takes two
# optional parameters: a player's name and how many goals he scored.
#  The program must be able to show the player's file, even if some
#  data has not been entered correctly.

def data(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '' or g.isalpha() is True:
        g = 0
    print(f'The player {n} scored {g} goals in the championship!')


print(30 * '-')
name = str(input("Player's name: ")).strip().capitalize()
goals = str(input("Number of goals: ")).strip()
data(name, goals)
