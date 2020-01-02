tupla = (
    'Learn',
    'Program',
    'Language',
    'Python',
    'Course',
    'Free',
    'Study',
    'Practice',
    'Work',
    'Market',
    'Programmer',
    'Future'
)

for i in tupla:
    print(f'\nIn word {i} we have the following vowels:', end=' ')
    for letter in i:
        if letter.lower() in 'aeiou':
            print(letter.upper(), end=' ')