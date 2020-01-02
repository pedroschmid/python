text = str(input('Type a text: ')).strip().upper()

word = text.split()
together = ''.join(word)
invertedWord = ''

for letter in range(len(together) - 1, -1, -1):
    invertedWord += together[letter]

if invertedWord == together:
    print(f'Typed: {together} | Inverted: {invertedWord} | its palindrome!')
else:
    print(f'Typed: {together} | Inverted: {invertedWord} | its not palindrome!')    