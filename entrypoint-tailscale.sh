#!/bin/sh
set -e

# Start tailscaled in userspace mode
/usr/local/bin/tailscaled --state=/tmp/tailscaled.state --tun=userspace-networking &

# Wait for tailscaled to be ready
sleep 5

# Run tailscale up with the auth key from environment
/usr/local/bin/tailscale up \
  --authkey=${TAILSCALE_AUTHKEY} \
  --hostname=render-node \
  --accept-routes \
  --accept-dns=false

# Keep the container alive
tail -f /dev/null
