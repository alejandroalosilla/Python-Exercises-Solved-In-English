#  Ex025 - Create a program that reads a person's name and says if they have
# "MENDES" in their name.

full_name = str(input('What is your full name? ')).strip().upper()
mendes_test = 'MENDES' in full_name

print(f'Does your name have "Mendes" in it? {mendes_test}')
