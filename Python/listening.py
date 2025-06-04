import socket
import ipServer

messaggi_ricevuti = []

def ascolta_server():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Consente riutilizzo
    s.bind((ipServer.IP_SERVER, 6100))  # Ascolta il server sulla porta 6100
    s.listen(1)

    try:
        while True:
            conn, addr = s.accept()
            dati = conn.recv(1024).decode()
            messaggio, IPDest = dati.split("|")
            conn.close()
            print("[UTENTE] MESSAGGIO RICEVUTO:", messaggio, "DA:", addr[0])
            messaggi_ricevuti.append({"mittente": addr[0], "messaggio": messaggio})
    finally:
        s.close()
