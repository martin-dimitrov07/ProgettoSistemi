import socket

def invia_messaggio(messaggio, IPDest):
    s = socket.socket()
    print(IPDest + " SENDER SERVER")
    s.connect((IPDest, 6100))  # IP e porta del server
    dati = f"{messaggio}|{IPDest}"
    s.send(dati.encode()) 
    s.close()