sex = str(input('Type your sex [M/F]: ')).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Invalid data, please type your sex again [M/F]: ')).strip().upper()[0]

print(f'Successfully registered sex!')