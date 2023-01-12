#  Ex097 - Write a program that has a function called write(), which takes
# any text as a parameter and displays a message with an adaptable
# size.

def write(msg):
    print((len(msg) + 2) * '~')
    print(f' {msg}')
    print((len(msg) + 2) * '~')


write('Alejandro Alosilla')
write('I will be back')
write('I love hamburgers and fries and a big glass of soda!')
