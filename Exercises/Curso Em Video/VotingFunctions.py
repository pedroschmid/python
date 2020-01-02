from datetime import datetime

def vote(years):
    age = datetime.now().year - years

    if 18 < age < 70:
        return f'With {age} years: MANDAROTY VOTE!'
    elif 15 < age < 17:
        return f'With {age} years: OPTIONAL VOTE!'
    else:
        return f'With {age} years: DENIED VOTE!'

print('=-' * 20)

years = int(input('Type the year you were born: '))
print(f'{vote(years)}')

print('=-' * 20)