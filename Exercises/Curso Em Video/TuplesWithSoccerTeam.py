tupla = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'AtleticoPR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Chapecoense')

print(f'The first 5 placed: {tupla[:5]}')
print(f'The last 4 placed: {tupla[-4:]}')
print(f'Teams in alphabetical order: {sorted(tupla)}')
print(f'Chapecoense team position: {tupla.index("Chapecoense")+1}')