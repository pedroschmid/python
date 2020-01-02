# coding:utf-8
import sys
import dns.resolver

argumentos = sys.argv # comando para ler os argumentos do comando

try:
    dominio = argumentos[1] # nome do dominio, exe: www.banco.com
    lista = argumentos[2] # nome da wordlist.txt

except: # se o try for invalido, entra no except e encerra o programa
    print("Faltam argumentos no comando")
    sys.exit(1)

# abre a wordlist
try: # try pra abrir a lista txt com os subdominios
    arquivo = open(lista) # abre a lista
    linha = arquivo.read().splitlines() # le as linhas da lista

except: # se o try for invalido, entra no except e encerra o programa
    print("Arquivo não encontrado")
    sys.exit(1)

# pra cada linha da wordlist, testa o dns
for linha in linha:
    subdominio = linha + '.' + dominio # cria o subdominio (www, admin, painel, etc)

    try:
        respostas = dns.resolver.query(subdominio, 'a') # faz um requisição em um subdominio pra procurar entradas de string "a"
        for resultado in respostas:
            print(subdominio, resultado)
    except:
        pass
