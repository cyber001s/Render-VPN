#!/bin/sh
set -e

echo "[INFO] Starting tailscaled..."
tailscaled --state=/tmp/tailscaled.state --tun=userspace-networking &

# Wait for tailscaled to boot
sleep 5

echo "[INFO] Authenticating to Tailscale..."
tailscale up \
  --authkey=${TAILSCALE_AUTHKEY} \
  --hostname=render-node \
  --accept-routes \
  --accept-dns=false

echo "[INFO] Starting Flask app..."
exec python /app.py
