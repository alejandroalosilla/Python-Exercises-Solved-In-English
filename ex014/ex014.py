#  Ex014 - Write a program that converts a temperature typed into
# degrees Celsius and converts to degrees Fahrenheit.

t_celsius = float(input('Enter the temperature in °C: '))
t_fahrenheit = (1.8 * t_celsius) + 32

print(f'A temperature of {t_celsius:.1f}ºC corresponds to {t_fahrenheit:.1f}ºF.')
