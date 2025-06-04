import socket
import costants

def invia_messaggio(messaggio, IPDest, porta):
    if porta is None:
        porta = costants.SOCKET_PORT
        
    try:
        # Crea socket
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(costants.SOCKET_TIMEOUT)
        
        # Connetti al destinatario
        my_socket.connect((IPDest, porta))
        
        # Gestione dati
        dati = f"{messaggio}|{IPDest}"
        my_socket.send(dati.encode('utf-8'))
        my_socket.close()
        
        print(f"[SENDER] Messaggio inviato a {IPDest}:{porta}")
        return "Messaggio inviato con successo"
        
    except socket.timeout:
        return f"Timeout nella connessione a {IPDest}:{porta}"
    except ConnectionRefusedError:
        return f"Connessione rifiutata da {IPDest}:{porta}"
    except Exception as e:
        return f"Errore nell'invio: {str(e)}"