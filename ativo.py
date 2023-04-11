import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() 

# conecta-se com o par passivo
sock.connect((HOST, PORTA)) 

# recebe a mensagem do usuario e envia para o passivo, se nao for fim
entrada = input()
while(entrada != 'fim'):
    # envia a mensagem para o passivo
    sock.send(entrada.encode())

    # pega a resposta do passivo e a imprime
    devolvida = sock.recv(1024)
    print(str(devolvida,  encoding='utf-8'))

    # recebe a proxima mensagem
    entrada = input()

# encerra a conexao
sock.close() 