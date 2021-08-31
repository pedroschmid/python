text = str(input('Type a text: ')).strip()
target = str(input('Type the wordkey you want to search: ')).strip()

print(f'The text has {target}? {target.upper() in text.upper()}')
