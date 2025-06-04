import threading

#globali
receivedMessages = []
lockMessage = threading.Lock()

def aggiungi_messaggio(mittente, messaggio, destinatario, tipo="ricevuto"):
    global receivedMessages
    
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
    global receivedMessages

    with lockMessage:
        return receivedMessages