import socket

# Crea socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Imposta la porta locale su cui ricevere (prima del send)
# sock.bind(("", 5007))  # "" significa tutte le interfacce locali

# CAPIRE IP SERVER

# Abilita broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Invia un messaggio in broadcast sulla porta 5007
messaggio = "DANIELE"
sock.sendto(messaggio.encode("utf-8"), ("255.255.255.255", 5007))

print("Messaggio broadcast inviato")

# Ricevi risposta
print("In attesa di risposta...")
dati, addr = sock.recvfrom(1024)



# # Invia messaggio
# messaggio = "VOGLIO MORIRE"
# dest_ip = addr[0]
# dest_port = 5007
# sock.sendto(messaggio.encode("utf-8"), (dest_ip, dest_port))

# print("Messaggio inviato al server")

# # Ricevi risposta
# print("In attesa di risposta...")
# dati, addr = sock.recvfrom(1024)

# # Decodifica e stampa
# risposta = dati.decode("utf-8")
# print("Risposta dal server:", risposta, "Addr:", addr)

sock.close()
