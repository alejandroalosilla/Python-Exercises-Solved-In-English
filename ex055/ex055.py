# Ex055 - Make a program that reads the weight of five people.
# At the end, show which was the highest and lowest weight read.

h_weight = 0
s_weight = 0

for c in range(1, 6):
    weight = float(input(f'Weight of the {c}° person: '))
    if weight > h_weight:
        h_weight = weight
    if c == 1:
        s_weight = weight
    if weight < s_weight:
        s_weight = weight

print(f'The highest weight read was {h_weight:.2f}kg')
print(f'The smallest weight read was {s_weight:.2f}kg')
