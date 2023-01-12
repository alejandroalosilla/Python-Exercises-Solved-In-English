#  Ex100 - Write a program that has a list called numbers and two functions
# called sort() and sum_pair().
#  The first function will draw 5 numbers and place them inside the
# list and the second function will show the sum of all the even values
# drawn by the previous function.

from time import sleep
from random import randint
lis = list()


def sort():
    for c in range(0, 5):
        lis.append(randint(1, 9))
        print(lis[c], end=' ')
        sleep(0.4)
    print('END!')


def sum_pair():
    sum_even = 0
    for c in lis:
        if c % 2 == 0:
            sum_even += c
    print(f'Summing the even values of the list {lis}, we have {sum_even}')


sort()
sum_pair()
