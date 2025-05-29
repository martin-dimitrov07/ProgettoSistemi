import socket

# C#
# Studente pippo = new Studente();

#INSTANZIAMO UN SOCKET UDB
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#BINDIAMO IL SOCKET CIOE' ASSOCIAMO UNA PORTA E UN INDIRIZZO AL SOCKET
# IN QUESTO CASO BINDIAMO IL SOCKET ALL'INDIRIZZO LOCALE
my_socket.bind(('127.0.0.1', 5007))
print("Server in ascolto...")

(messaggio, addr)=my_socket.recvfrom(1024) #BUFFER SIZE
#Restituisce il messaggio ricevuto e l'indirizzo del client
msg = messaggio.decode("utf-8") #decodifica il messaggio in bytes in stringa
print(msg)


#####

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_addr = ("127.0.0.1", 5007)
my_socket.bind(socket_addr)

my_socket.recvfrom(1024) #misura buffer (finestra per vedere se qualcuno si connette)

