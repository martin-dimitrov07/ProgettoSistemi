# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/saluta", methods=["GET"])
def saluta():
    nome = request.args.get("nome", "ospite")
    return jsonify({"messaggio": f"Ciao {nome}!"})

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
