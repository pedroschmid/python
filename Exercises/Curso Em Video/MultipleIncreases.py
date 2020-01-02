salary = float(input('Type your salary: '))

if salary > 1250.00:
    salary = salary + (salary * 0.10)
    print(f'The salary with increase is ${salary}')
else:
    salary = salary + (salary * 0.15)
    print(f'The salary with increase is ${salary}')