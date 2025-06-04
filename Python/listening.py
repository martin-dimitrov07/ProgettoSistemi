import socket
import threading
import constants
import messageStorage

server_running = False
server_socket = None
server_thread = None

def start_listening_server():
    global server_running, server_thread
    
    if server_running:
        return "Server già in ascolto"
    
    server_running = True
    server_thread = threading.Thread(target=listenServerLoop)
    server_thread.daemon = True
    server_thread.start()
    
    print(f"[LISTENING-SERVER] Server avviato su {constants.SERVER_HOST}:{constants.SOCKET_PORT}")
    return "Server di ascolto avviato"

def start_listening_client():
    client_thread = threading.Thread(target=listenLoop)
    client_thread.daemon = True
    client_thread.start()

    return "Server di ascolto avviato"

def listenLoop():
    try:
        # Crea e configura socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # permette il riutilizzo della porta anche se è in stato TIME_WAIT (occupata).
        client_socket.bind((constants.IP_SERVER, constants.SOCKET_PORT))
        client_socket.listen(5) # numero massimo di connessioni in attesa di accept()
        
        print(f"[LISTENING-CLIENT] In ascolto sulla porta {constants.SOCKET_PORT}")
        
        while True:
            try:
                # Timeout per permettere controllo del server_running
                client_socket.settimeout(constants.LISTEN_TIMEOUT) # quanto tempo aspettare prima che dia errore
                conn, addr = client_socket.accept()
                
                # Gestisci il messaggio in un thread separato
                thread = threading.Thread(target=income_message, args=(conn, addr))
                thread.daemon = True
                thread.start()
                
            except socket.timeout:
                # continua il loop
                continue
            except Exception as e:
                if server_running:
                    print(f"[ERRORE LISTENING-CLIENT] Errore nell'accettare connessione: {e}")
                
    except Exception as e:
        print(f"[ERRORE LISTENING-CLIENT] Errore nel server di ascolto: {e}")
    finally:
        if server_socket:
            server_socket.close()
        # server_running = False



def listenServerLoop():
    global server_socket, server_running
    
    try:
        # Crea e configura socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # permette il riutilizzo della porta anche se è in stato TIME_WAIT (occupata).
        server_socket.bind((constants.SERVER_HOST, constants.SOCKET_PORT))
        server_socket.listen(5) # numero massimo di connessioni in attesa di accept()
        
        print(f"[LISTENING-SERVER] In ascolto sulla porta {constants.SOCKET_PORT}")
        
        while server_running:
            try:
                # Timeout per permettere controllo del server_running
                server_socket.settimeout(constants.LISTEN_TIMEOUT) # quanto tempo aspettare prima che dia errore
                conn, addr = server_socket.accept()
                
                # Gestisci il messaggio in un thread separato
                thread = threading.Thread(target=income_message, args=(conn, addr))
                thread.daemon = True
                thread.start()
                
            except socket.timeout:
                # continua il loop
                continue
            except Exception as e:
                if server_running:
                    print(f"[ERRORE LISTENING-SERVER] Errore nell'accettare connessione: {e}")
                
    except Exception as e:
        print(f"[ERRORE LISTENING-SERVER] Errore nel server di ascolto: {e}")
    finally:
        if server_socket:
            server_socket.close()
        # server_running = False

    

def income_message(conn, addr):
    # gestisce singolo messaggio ricevuto
    try:
        # Ricevi dati
        data = conn.recv(1024).decode('utf-8')

        if data:
            # messaggio formato: messaggio|IP_destinatario
            if len(data.split("|")) >= 1:
                messaggio, IPDest = data.split("|")

                if messaggio:
                    messageStorage.aggiungi_messaggio(
                        mittente=addr[0],
                        messaggio=messaggio,
                        destinatario=IPDest,
                        tipo="ricevuto"
                    )
                    
                    print(f"Messaggio ricevuto da {addr}: {messaggio}")
                    
    except Exception as e:
        print(f"[ERRORE LISTENING] Errore nella gestione del messaggio da {addr}: {e}")
    finally:
        try:
            conn.close()
        except:
            pass