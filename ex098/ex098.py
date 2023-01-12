#  Ex098 - Write a program that has a function called counter(), which takes
# three parameters: start, end and step.
#  Your program has to perform three counts through the created
# function:
#
# a) from 1 to 10, 1 by 1
# b) from 10 to 0, 2 by 2
# c) a custom count

from time import sleep


def p():
    print(15 * '-=')


def counter1_10_1():
    sleep(1)
    p()
    print('Counting from 1 to 10 1 by 1')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.4)
    print('END!')


def counter10_0_2():
    sleep(1)
    p()
    print('Count from 10 to 0 by 2 by 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.4)
    print('END!')


def custom_count():
    sleep(1)
    p()
    print('Custom Count!')
    start = int(input('Start: '))
    end = int(input('End: '))
    step = abs(int(input('Step: ')))
    if step == 0:
        step = 1

    if start > end:
        for c in range(start, end - 1, -1 * step):
            print(c, end=' ')
            sleep(0.4)
        print('END!')
    else:
        for c in range(start, end + 1, step):
            print(c, end=' ')
            sleep(0.4)
        print('END!')


counter1_10_1()
counter10_0_2()
custom_count()
