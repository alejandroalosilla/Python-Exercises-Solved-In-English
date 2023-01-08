#  Ex043 - Develop a logic that reads a person's weight and height,
# calculates their Body Mass Index (BMI) and displays their
# status, according to the table below:
# - BMI below 18.5: Underweight
# - Between 18.5 and 25: Ideal Weight
# - 25 to 30: Overweight
# - 30 to 40: Obesity
# - Above 40: Morbid obesity

weight = float(input('What is your weight? (Kg) '))
height = float(input('What is your height? (m) '))
bmi = weight / (pow(height, 2))

print(f'This person is BMI is {bmi:.1f}')

if bmi < 18.5:
    print('Underweight')
elif 18.5 < bmi <= 25:
    print('Ideal Weight')
elif 25 < bmi <= 30:
    print('Overweight')
elif 30 < bmi <= 40:
    print('Obesity')
else:
    print('Morbid obesity')
