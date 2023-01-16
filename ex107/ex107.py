#  Ex107 - Create a module called coin.py that has built-in functions
# half(), double(), increase() and decrease().
#  Also write a program that imports this module and uses some of these
# functions.

import coin

p = float(input('Enter price: $'))
print(f'Half of ${p} is {coin.half(p)}')
print(f'The double of ${p} is ${coin.double(p)}')
print(f'Increasing by 10% we get ${coin.increase(p)}.')
print(f'Decreasing 10%, we have ${coin.decrease(p)}.')
