age = int(input('сколько тебе лет? '))

if age % 10 == 0:
    print(age, 'лет')
elif age % 10 > 4:
    print(age, 'лет')
elif age > 10 and age < 15:
    print(age, 'лет')
elif age % 10 == 1 and age != 11:
    print(age, 'год')
else:
    print(age, 'года')
