import threading

#globali
receivedMessages = []
lockMessage = threading.Lock()

def aggiungi_messaggio(mittente, messaggio, destinatario, tipo="ricevuto"):
    with lockMessage:
        newMessage = {
            "mittente": mittente,
            "messaggio": messaggio,
            "destinatario": destinatario,
            "tipo": tipo
        }
            
        receivedMessages.append(newMessage)
        return newMessage
    
def get_messaggi():
    with lockMessage:
        return receivedMessages