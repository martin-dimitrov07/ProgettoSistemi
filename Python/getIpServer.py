from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/ip")
def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return jsonify({"ip": ip})

app.run(port=5000)
