#  Ex112 - Within the utilitiesCeV package we created in challenge 111, we
# have a module called data.
#  Create a function called readmoney() that is able to work like the
# input() function, but with data validation to only accept values that
# are monetary.

from utilitiesCeV import coin
from utilitiesCeV import data

p = data.readmoney('Enter price: $')
coin.summary(p, 15, 15)
