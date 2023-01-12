#  Ex099 - Make a program that has a function called bigger(), which receives
# several parameters with integer values.
#  Your program has to look at all the values and say which one is the
# largest.

from time import sleep


def bigger(*lst):
    print(30 * '-=')
    print('Analyzing the values...')
    if len(lst) != 0:
        for c in lst:
            print(c, end=' ')
            sleep(0.4)
        print(f'A total of {len(lst)} values were reported.')
        print(f'The highest reported value was {max(lst)}.')
    else:
        print(f'A total of 0 values were reported.')
        print(f'The highest reported value was 0.')


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger()
