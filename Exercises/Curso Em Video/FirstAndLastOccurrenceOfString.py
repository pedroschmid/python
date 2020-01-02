text = str(input('Type a text: ')).strip()
letter = str(input('type a letter you want to find: ')).strip()
length = len(text)

print(f'How many times {letter} appears? {text.count(letter)}')
print(f'What position {letter} appears? {text.find(letter) + 1}')
print(f'What position {letter} appeared the last time? {text.rfind(letter) + 1}')
