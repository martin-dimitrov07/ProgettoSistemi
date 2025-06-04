import socket
import ipServer

def invia_messaggio(messaggio, IPDest):
    s = socket.socket()
    s.connect((ipServer.IP_SERVER, 6000))  # IP e porta del server
    dati = f"{messaggio}|{IPDest}"
    s.send(dati.encode()) 
    s.close()