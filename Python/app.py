from flask import Flask, request, jsonify
from flask_cors import CORS
import listeningServer, listening, sender

app = Flask(__name__)
CORS(app) # Permette richieste da origini diverse (es. pagine HTML locali)

@app.route("/api/invia", methods=["POST"])
def invia():
    messaggio = request.json.get("messaggio")
    IPmittente = request.json.get("IPmittente")
    sender.invia_messaggio(messaggio, IPmittente)
    return jsonify({"status": "Messaggio inviato"})


@app.route("/api/ascoltaServer", methods=["POST"])
def ascolta():
    # Avvia il server di ascolto
    listeningServer.avvia_server()

    return jsonify({"status": "Server di ascolto avviato"})

@app.route("/api/ascolta", methods=["POST"])
def ascolta_server():
    messaggio = listening.ascolta_server()

    return jsonify({"messaggio": messaggio})

# serve per accedere dal browser al server Flask app.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
