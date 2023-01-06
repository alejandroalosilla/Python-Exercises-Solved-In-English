#  Ex036 - Write a program to approve the bank loan for the purchase
# of a house. Ask the home's value, the buyer's salary and in
# how many years he will pay. The monthly installment cannot
# exceed 30% of the salary or else the loan will be denied.

house_value = float(input('House value: $'))
buyer_salary = float(input('Buyer Salary: $'))
years = int(input('How many years of financing? '))

month_installment = house_value / (12 * years)

if month_installment < (0.3 * buyer_salary):
    print(f'To pay off a ${house_value:.2f} house over {years} years the down payment will be ${month_installment:.2f}')
    print('Loan can be granted!')
else:
    print(f'To pay off a ${house_value:.2f} house over {years} years the down payment will be ${month_installment:.2f}')
    print('Loan denied!')
