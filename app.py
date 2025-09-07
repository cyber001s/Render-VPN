from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

# Healthcheck endpoint
@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

# Admin endpoint to generate WireGuard client config
@app.route('/generate-client', methods=['POST'])
def generate_client():
    data = request.get_json() or {}
    client_name = data.get('name', 'client1')
    from wg_gen import generate_client_conf
    conf = generate_client_conf(client_name)
    return jsonify({'client_conf': conf})

# Basic uptime endpoint
@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'running', 'hostname': os.uname().nodename})

# Tailscale info endpoint
@app.route('/tailscale', methods=['GET'])
def tailscale_info():
    try:
        out = subprocess.check_output(['tailscale', 'status', '--json'])
        return out, 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
