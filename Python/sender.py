import socket
import costants

def invia_messaggio(messaggio, IPDest, porta):
    if porta is None:
        porta = costants.SOCKET_PORT
        
    try:
        # Crea socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(costants.SOCKET_TIMEOUT)

        # Connetti al destinatario
        s.connect((str(IPDest), int(porta)))
        
        # Gestione dati
        dati = f"{messaggio}|{IPDest}"
        s.send(dati.encode('utf-8'))
        s.close()
        
        print(f"[SENDER] Messaggio inviato a {IPDest}:{porta}")
        return "Messaggio inviato con successo"
        
    except socket.timeout:
        return f"Timeout nella connessione a {IPDest}:{porta}"
    except ConnectionRefusedError:
        return f"Connessione rifiutata da {IPDest}:{porta}"
    except Exception as e:
        return f"Errore nell'invio: {str(e)}"