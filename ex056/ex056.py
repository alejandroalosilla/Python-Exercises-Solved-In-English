#  Ex056 - Develop a program that reads the name, age and gender
# of 4 people.
#  At the end of the program, show: the average age of the group,
# what is the name of the oldest man and how many women are under
# 20 years old.

sum_ages = 0
oldest_man_age = 0
oldest_man_name = ''
woman_under_20 = 0

for c in range(1, 5):
    print(f'----{c}º PERSON----')
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender[M/F]: ')).upper().strip()

    sum_ages += age

    if age > oldest_man_age and gender == 'M':
        oldest_man_age = age
        oldest_man_name = name
    if age < 20 and gender == 'F':
        woman_under_20 += 1

average = sum_ages / 4

print(f'The average age of the group is {average:.1f} years old')
print(f'The oldest man is {oldest_man_age} years old and his name is {oldest_man_name}')
print(f'In all, there are {woman_under_20} women under the age of 20')
