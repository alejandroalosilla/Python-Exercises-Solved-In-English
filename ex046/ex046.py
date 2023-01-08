#  Ex046 - Write a program that displays a countdown for the burst of
# fireworks on screen, going from 10 to 0, with a 1-second pause
# between them.
from time import sleep
from emoji import emojize

# colors:
blue = '\033[34m'
red = '\033[31m'

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize(f'{blue}BOOM! BOOM! POOOW!:fireworks::fireworks::fireworks:'))
print(emojize(f'{red}Happy New Year!:sparkler::sparkler::sparkler:'))
