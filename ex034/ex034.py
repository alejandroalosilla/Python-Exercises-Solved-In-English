#  Ex034 - Write a program that asks for an employee's salary and calculates
# the amount of his raise.
# For salaries greater than $1250.00, calculate a 10% increase.
# For inferior or equal, the increase is 15%.

salary = float(input("What is the employee's salary? $"))
new_salary = 0

if salary > 1250:
    new_salary = salary + (salary * 0.1)
else:
    new_salary = salary + (salary * 0.15)

print(f'Those who earned ${salary:.2f} now earn ${new_salary:.2f}!')
