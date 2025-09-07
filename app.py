from flask import Flask, request, jsonify
import os
import subprocess


app = Flask(__name__)


# Healthcheck endpoint (UptimeRobot will ping this)
@app.route('/health', methods=['GET'])
def health():
return 'OK', 200


# Small admin endpoint to generate WireGuard client config (calls wg_gen.py logic)
# WARNING: This only generates files, does NOT start a server on Render.
@app.route('/generate-client', methods=['POST'])
def generate_client():
data = request.get_json() or {}
client_name = data.get('name', 'client1')
# For safety, we only return config text. Real key handling should be done on a secure VPS.
from wg_gen import generate_client_conf
conf = generate_client_conf(client_name)
return jsonify({'client_conf': conf})


# Basic uptime endpoint
@app.route('/status', methods=['GET'])
def status():
return jsonify({'status': 'running', 'hostname': os.uname().nodename})


if __name__ == '__main__':
app.run(host='0.0.0.0', port=10000)
