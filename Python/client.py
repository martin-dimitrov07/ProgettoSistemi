import socket  #socket = connettore che c'è sopra il livello 4 (l'utente può attaccarsi con APP)

# TCP / UDP = livello 4

# socket definito da IP e PORTA (da 0 a 65.535 => su 16 bit) ==> tupla IP - PORTA

# Creazione del socket UDP
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket ha metodo che si chiama socket che si aspetta come parametri delle classi

# Invia il messaggio direttamente con sendto()
my_socket.sendto("Hello, server!".encode("utf-8"), ("127.0.0.1", 5007)) # funziona sempre (mandi a te stesso) ; PORTA numero che vuoi da 1024 in poi

print("Messaggio inviato al server.")
# Chiudi il socket (buona pratica)
my_socket.close()

