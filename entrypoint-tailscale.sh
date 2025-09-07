#!/bin/sh

# This script starts tailscaled in userspace mode and then tailscale up
# On Render you'll need to obtain an auth key or use interactive auth
#set -e


# Example: download tailscale binary (update version as needed)
 #curl -fsSL https://pkgs.tailscale.com/stable/tailscale_1.64.0_amd64.tgz | tar xz -C /usr/local/bin --strip-components=1
# Start tailscaled in foreground (userspace-mode) and then run tailscale up --authkey $TAILSCALE_AUTHKEY
# For full steps see README-Tailscale.md


#exec tailscaled --state=/tmp/tailscaled.state --tun=userspace-networking



# Use the Render example approach: run Tailscale userspace client
FROM alpine:3.18

RUN apk add --no-cache curl bash iproute2

# Install Tailscale (static binary, latest stable)
RUN curl -fsSL https://pkgs.tailscale.com/stable/tailscale_1.64.0_amd64.tgz \
    | tar xz -C /usr/local/bin --strip-components=1

COPY entrypoint-tailscale.sh /entrypoint-tailscale.sh
RUN chmod +x /entrypoint-tailscale.sh

EXPOSE 80
CMD ["/entrypoint-tailscale.sh"]
