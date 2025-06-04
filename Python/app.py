import socket
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import utilities
import messageStorage
import sender
import listening
import costants

app = Flask(__name__)
CORS(app) # Permette richieste da origini diverse (es. pagine HTML locali)

@app.route("/api/invia", methods=["POST"])
def invia():
    # inviare messaggi
    try:
        # Ottieni dati dalla richiesta
        data = request.get_json() # converte in dizionario
        if not data:
            return jsonify({"error": "Dati JSON mancanti"}), 400
            
        # se non c'è da vuoto e .strip() rimuove spazi all'inizio e fine
        messaggio = data.get("messaggio", "").strip() 
        ip_dest = data.get("IPDest", "").strip()
        
        # Validazione input
        if not messaggio:
            return jsonify({"error": "Il messaggio non può essere vuoto"}), 400 # 400: Bad Request
        if not ip_dest:
            return jsonify({"error": "IP destinatario obbligatorio"}), 400
        
        # Invia messaggio in modo asincrono
        # sender.invia_messaggio_async(messaggio, ip_dest)
        thread = threading.Thread(target=sender.invia_messaggio, args=( messaggio, ip_dest, costants.SOCKET_PORT ))
        thread.daemon = True # chiude automaticamente quando il thread termina
        thread.start()
        
        # Aggiungi il messaggio inviato al storage locale
        messaggio_inviato = messageStorage.aggiungi_messaggio(
            mittente=utilities.GetIp(),
            messaggio=messaggio,
            destinatario=ip_dest,
            tipo="inviato"
        )
        
        return jsonify({
            "status": "Messaggio inviato",
            "messaggio": messaggio_inviato
        })
        
    except Exception as e:
        print(f"[API-INVIA] Error: {e}")
        return jsonify({"error": f"Errore interno: {str(e)}"}), 500 #500: Internal error


@app.route("/api/ascoltaServer", methods=["POST"])
def ascolta():
    # avvio listening del server
    try:
        result = listening.start_listening_server()
        return jsonify({"status": result})
    except Exception as e:
        print(f"[API-SERVERASCOLTTA] Error: {e}")
        return jsonify({"error": f"Errore nell'avvio del server: {str(e)}"}), 500
    
    
@app.route("/api/ascolta", methods=["POST"])
def ascolta():
    # avvio listening del server
    try:
        result = listening.start_listening_client()
        return jsonify({"status": result})
    except Exception as e:
        print(f"[API-CLIENTASCOLTA] Error: {e}")
        return jsonify({"error": f"Errore nell'avvio del server: {str(e)}"}), 500
    


@app.route("/api/messaggi", methods=["GET"])
def get_messaggi():
    # tutti i messaggi per IP
    try:
        ip_filtro_mittente = request.args.get("IPMittente")
        messaggi = messageStorage.get_messaggi(ip_filtro_mittente)
        
        return jsonify({
            "messaggi": messaggi
        })
        
    except Exception as e:
        print(f"[API-MESSAGGI] Errore in get_messaggi: {e}")
        return jsonify({"error": f"Errore nel recupero messaggi: {str(e)}"}), 500

# serve per accedere dal browser al server Flask app.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
