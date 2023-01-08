#  Ex044 - Create a program that calculates the amount to be paid for a
# product, considering its normal price and payment terms:
# - cash/check: 10% discount
# - cash on the card: 5% discount
# - in up to 2 installments on the card: formal price
# - 3x or more on the card: 20% interest

print('======= TEST STORE =======')
price = float(input('Purchase price: $'))
print('PAYMENT METHODS:')
print('[1] in cash')
print('[2] Card debit')
print('[3] 2x on credit')
print('[4] 2x or more on credit')
option = int(input('What is the option? '))
new_price = 0

if option == 1:
    new_price = price - (0.1 * price)
elif option == 2:
    new_price = price - (0.05 * price)
elif option == 3:
    new_price = price
elif option == 4:
    new_price = price + (0.2 * price)

print(f'Your ${price:.2f} purchase will cost you ${new_price:.2f} in the end.')
