#  Ex108 - Adapt the code from challenge #107, creating an additional function
# called currency() that can display numbers as a formatted monetary
# value.

import coin

p = float(input('Enter price: $'))
print(f'Half of {coin.currency(p)} is {coin.currency(coin.half(p))}')
print(f'The double of {coin.currency(p)} is {coin.currency(coin.double(p))}')
print(f'Increasing by 10% we get {coin.currency(coin.increase(p))}')
print(f'Decreasing 10%, we have {coin.currency(coin.decrease(p))}')
