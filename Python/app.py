from flask import Flask, request, jsonify
from flask_cors import CORS
import listeningServer, listening, sender
from listening import messaggi_ricevuti  # importa la lista condivisa
import threading

app = Flask(__name__)
CORS(app) # Permette richieste da origini diverse (es. pagine HTML locali)

@app.route("/api/invia", methods=["POST"])
def invia():
    messaggio = request.json.get("messaggio")
    IPDest = request.json.get("IPDest")
    thread_invia = threading.Thread(target=sender.invia_messaggio, args=(messaggio, IPDest))
    thread_invia.start()

    sender.invia_messaggio(messaggio, IPDest)
    return jsonify({"status": "Messaggio inviato"})


@app.route("/api/ascoltaServer", methods=["POST"])
def ascolta():
    # Avvia il server di ascolto
    thread = threading.Thread(target=listeningServer.avvia_server)
    thread.daemon = True # chiude automaticamente quando l'app termina
    thread.start()

    return jsonify({"status": "Server di ascolto avviato"})

@app.route("/api/ascolta", methods=["POST"])
def ascolta_server():
    messaggio = listening.ascolta_server()

    return jsonify({"messaggio": messaggio})

@app.route("/api/messaggi", methods=["GET"])
def get_messaggi():
    IP = request.args.get("IP")
    messaggi = {}
    for m in messaggi_ricevuti:
        if m["mittente"] == IP:
            messaggi.append(m)
    return jsonify({"messaggi": messaggi})

# serve per accedere dal browser al server Flask app.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
