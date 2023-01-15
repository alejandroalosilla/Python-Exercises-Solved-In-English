#  Ex106 - Make a mini-system that uses Python's Interactive Help.
#  The user will type the command and the manual will appear.
#  When the user types the word 'END', the program will exit.
#  Important: use color.

from time import sleep


def print_lines(msg, c):
    print(f'\033[{c}m', (len(msg) + 4) * '-')
    print(f'  {msg}')
    print((len(msg) + 4) * '-', '\n\033[m', end='')
    sleep(2)


def pyhelp():
    function = 'start'
    while function != 'end':
        print_lines('PyHELP HELP SYSTEM', 42)
        function = str(input('Function or library: ')).strip().lower()
        print_lines(f"Accessing the '{function}' command manual", 44)
        print('\033[7m')
        help(function)
        print('\033[m')
        sleep(2)


pyhelp()
