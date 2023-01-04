#  Ex004 - Write a program that reads something from the
# keyboard and displays its primitive type and all
# possible information about it on the screen.

something = input('Type something: ')

print(f'The primitive type of this value is: {type(something)}')
print(f'Just spaces? {something.isspace()}')
print(f'Is it a number? {something.isnumeric()}')
print(f'Is it alphabetical? {something.isalpha()}')
print(f'Is it alphanumeric? {something.isalnum()}')
print(f'Is everything capitalized? {something.isupper()}')
print(f'Is it lowercase? {something.islower()}')
print(f'Is it capitalized? {something.istitle()}')
