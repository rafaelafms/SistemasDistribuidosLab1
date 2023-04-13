import socket

HOST = ''     # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5000  # porta onde chegarao as mensagens para essa aplicacao

# cria um socket para comunicacao
sock = socket.socket() 

# vincula a interface e porta para comunicacao
sock.bind((HOST, PORTA))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
sock.listen(5) 

print("Pronto para receber conexões...")

# aceita a primeira conexao da fila 
novoSock, endereco = sock.accept() # retorna um novo socket e o endereco do par conectado
print ('Conectado com: ', endereco)

while True:
	# depois de conectar-se, recebe a mensagem 
	msg = novoSock.recv(1024) 
	# sem mensagem, encerra o passivo
	if not msg: break 
	# envia a mensagem de volta para o ativo
	else:
		# print("Mensagem recebida: " + str(msg,  encoding='utf-8'))
		novoSock.send(msg)
		# print("Mensagem enviada: " + str(msg,  encoding='utf-8'))

# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close() 