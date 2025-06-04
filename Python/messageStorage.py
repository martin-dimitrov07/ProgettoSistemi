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
    
def get_messaggi(ipMittente):
    with lockMessage:
        return [
            m for m in receivedMessages 
            if m.get("mittente") == ipMittente
        ]