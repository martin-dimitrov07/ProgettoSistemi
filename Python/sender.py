import socket

def invia_messaggio(messaggio, IPDest):
    s = socket.socket()
    s.connect(("192.168.1.3", 6000))  # IP e porta del server
    dati = f"{messaggio}|{IPDest}"
    s.send(dati.encode()) 
    s.close()