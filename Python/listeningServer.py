import socket
import senderServer
import threading

users = []  # Lista per tenere traccia degli utenti connessi

def avvia_server():
    global users
    print("[SERVER] Avvio server socket...")

    s = socket.socket()
    s.bind(("0.0.0.0", 6000))  # Ascolta su tutte le interfacce sulla porta 6000
    s.listen(1)

    print("[SERVER] In ascolto sulla porta 6000")

    while True:
        conn, addr = s.accept()
        print(f"[SERVER] Connessione da {addr}")
        # if addr not in users:
        #     users.append(addr)
        dati = conn.recv(1024).decode()
        messaggio, IPDest = dati.split("|")
        thread = threading.Thread(target=senderServer.invia_messaggio, args=(messaggio, IPDest))
        thread.start()
        conn.close()
