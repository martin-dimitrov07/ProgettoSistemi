import socket

def invia_messaggio(messaggio, IPDest):
    s = socket.socket()
    s.connect((IPDest, 6000))  # IP e porta del server
    s.send(messaggio.encode()) 
    s.close()