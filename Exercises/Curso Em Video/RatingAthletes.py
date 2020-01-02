age = int(input('Type your age: '))

if age <= 9:
    print('Mirim')
elif 9 < age <= 14:
    print('Childish')
elif 14 < age <= 19:
    print('Junior')
elif 19 < age <= 20:
    print('Sênior')
else:
    print('Master')