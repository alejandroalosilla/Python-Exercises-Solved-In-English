#  Ex059 - Create a program that reads two values and displays a menu on
# the screen:
# [ 1 ] add
# [ 2 ] multiply
# [ 3 ] bigger
# [ 4 ] new numbers
# [ 5 ] Exit the program
#  Your program should perform the requested operation in each case.

from time import sleep

first_value = int(input('First value: '))
second_value = int(input('Second value: '))
menu_option = 0
while menu_option != 5:
    print('[1] sum')
    print('[2] multiply')
    print('[3] bigger')
    print('[4] new numbers')
    print('[5] Exit the program')
    menu_option = int(input('>>>>> What is your option? '))

    if menu_option == 1:
        print(f'The sum between {first_value} and {second_value} is {first_value + second_value}.')
        print(10 * '=-=')
        sleep(2.5)
    if menu_option == 2:
        print(f'The multiplication between {first_value} and {second_value} is {first_value * second_value}.')
        print(10 * '=-=')
        sleep(2.5)
    if menu_option == 3:
        if first_value > second_value:
            print(f'Between {first_value} and {second_value} the highest value is {first_value}.')
            print(10 * '=-=')
            sleep(2.5)
        elif second_value > first_value:
            print(f'Between {first_value} and {second_value} the highest value is {second_value}.')
            print(10 * '=-=')
            sleep(2.5)
        else:
            print('The two values are equal!')
            print(10 * '=-=')
            sleep(2.5)
    if menu_option == 4:
        first_value = int(input('First value: '))
        second_value = int(input('Second value: '))
    if menu_option < 1 or menu_option > 5:
        print('Invalid option. Try again!')
        print(10 * '=-=')
        sleep(2.5)
print('Ending the program...')
sleep(2.5)
print('End of program!')
