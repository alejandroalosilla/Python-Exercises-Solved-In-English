#  Ex024 - Create a program that reads the name of a city and says
# whether it starts with the name "SAN".

city_name = str(input('What city were you born in? ')).strip().upper().split()
san_test = 'SAN' in city_name[0]
print(f'Does the name of the city begin with the word "SAN"? {san_test}')
