# servizio_server.py

import socket

def avvia_server():
    print("[SERVER] Avvio server socket...")

    s = socket.socket()
    s.bind(("0.0.0.0", 6000))  # Ascolta su tutte le interfacce sulla porta 6000
    s.listen(1)

    print("[SERVER] In ascolto sulla porta 6000")

    while True:
        conn, addr = s.accept()
        print(f"[SERVER] Connessione da {addr}")
        dati = conn.recv(1024).decode()
        print(f"[SERVER] Ricevuto: {dati}")
        conn.send(f"Hai detto: {dati}".encode())
        conn.close()

avvia_server()
