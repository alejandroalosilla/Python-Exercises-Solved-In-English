#  Ex013 - Write an algorithm that reads an employee's salary and
# outputs their new salary, with a 15% increase.

salary = float(input("What is the employee's salary? $"))
new_salary = salary + (0.15 * salary)

print(f'An employee who earned ${salary:.2f}, with a 15% increase, now earns ${new_salary:.2f}.')
