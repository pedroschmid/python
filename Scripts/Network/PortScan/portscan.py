import socket # Modulo python para conexões de redes

portas = [21, 23, 80, 443, 8080] # Lista de portas

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # criando um objeto do tipo socket com protocolo TCP/IP
    cliente.settimeout(1)  # Vai tentar fazer o scan por 0.1s
    codigo = cliente.connect_ex(('bancocn.com', porta))  # Conecta o dominio com a porta para testar a conexão
    if codigo == 0:
        print(porta, "OPEN")
    