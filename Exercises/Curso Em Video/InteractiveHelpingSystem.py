from time import sleep
def linha():
    print('~' * 30)
print('\033[47m')
linha()
print('SISTEMA DE AJUDA PyHELP')
linha()
print('\033[m')
sleep(1)
def manual(comando):
    print('\033[44m')
    linha()
    print(f'Acessando o manual do comando `{comando}`')
    linha()
    print('\033[m')
    sleep(1)
    print('\033[7m')
    help(comando)
    print('\033[m')
while True:
    condicao = str(input('Função ou biblioteca > ')).lower().strip()
    if condicao == 'fim':
        print('\033[30;41mFim do programa!\033[m')
        break
    else:
        manual(condicao)