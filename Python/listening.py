# servizio_server -> listeningServer.py

import socket
import senderServer

def ascolta_server():
    s = socket.socket()
    s.bind(("192.168.1.3", 6001))  # Ascolta il server sulla porta 6001
    s.listen(1)

    while True:
        conn, addr = s.accept()
        dati = conn.recv(1024).decode()
        messaggio, IPDest = dati.split("|")
        conn.close()
        return messaggio
