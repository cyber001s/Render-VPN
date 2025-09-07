"""
Simple WireGuard config generator. Generates a server keypair (in memory) and a client config.
This script is for generating the .conf files quickly and printing them to stdout.
Do NOT run WireGuard on Render; use this on a VPS (Hetzner, Linode, Oracle free tier, etc.).
"""
import subprocess
import tempfile
import os


def generate_keypair():
p1 = subprocess.run(['wg', 'genkey'], capture_output=True, text=True, check=True)
private = p1.stdout.strip()
p2 = subprocess.run(['wg', 'pubkey'], input=private.encode(), capture_output=True, check=True)
public = p2.stdout.strip()
return private, public


def generate_client_conf(name='client1', server_pub='', server_endpoint='vpn.example.com:51820', client_ip='10.0.0.2/32'):
# In many environments wg binary exists. This function will fallback to a simple placeholder if not.
try:
priv, pub = generate_keypair()
except Exception:
priv = 'CLIENT_PRIVATE_KEY_PLACEHOLDER'
pub = 'CLIENT_PUBLIC_KEY_PLACEHOLDER'
conf = f"""
[Interface]
PrivateKey = {priv}
Address = {client_ip}
DNS = 1.1.1.1


[Peer]
PublicKey = {server_pub}
Endpoint = {server_endpoint}
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
"""
return conf


if __name__ == '__main__':
print(generate_client_conf())
