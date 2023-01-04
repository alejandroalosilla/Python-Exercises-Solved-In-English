#  Ex010 - Create a program that reads how much money a person
# has in their wallet and shows how many euros they can buy.

wallet_money = float(input('How much money do you have in your wallet? US$'))
euros = wallet_money * 0.96

print(f'With ${wallet_money:.2f} dollar(s) you can buy €{euros:.2f} euro(s).')
