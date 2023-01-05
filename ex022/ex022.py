#  Ex022 - Create a program that reads a person's full name and prints:
# - The name in all uppercase and lowercase letters.
# - How many letters in all (without considering spaces).
# - How many letters are in the first name.

full_name = str(input('Enter your full name: ')).strip()
name_without_spaces = full_name.replace(' ', '')
name_split = full_name.split()


print('Analyzing your name...')
print(f'Your name in capital letters is {full_name.upper()}')
print(f'Your lowercase name is {full_name.lower()}')
print(f'Your name has a total of {len(name_without_spaces)} letters.')
print(f'Your first name is {name_split[0]} and he has {len(name_split[0])} letters.')
