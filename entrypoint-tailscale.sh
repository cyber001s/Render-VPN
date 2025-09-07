#!/bin/sh
set -e

# Start tailscaled in userspace networking mode
tailscaled --state=/tmp/tailscaled.state --tun=userspace-networking &

# Give tailscaled a moment to start
sleep 5

# Bring up Tailscale client with your auth key
tailscale up \
  --authkey=${TAILSCALE_AUTHKEY} \
  --hostname=render-node \
  --accept-routes \
  --accept-dns=false

# Keep container running
wait -n
