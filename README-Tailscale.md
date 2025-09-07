# Run Tailscale on Render (recommended)


Render does not allow privileged kernel features like /dev/net/tun in typical web services, so a native WireGuard server often fails. Tailscale offers a userspace approach (userspace networking) and Render maintainers provide an example.


Reference: https://github.com/render-examples/tailscale


Steps:
1. Create a new Web Service on Render using Dockerfile.tailscale.
2. Provide a TAILSCALE_AUTHKEY as a secret environment variable (from the Tailscale admin panel).
3. Start tailscaled in userspace-networking mode and `tailscale up --authkey $TAILSCALE_AUTHKEY --accept-routes` to act as a subnet router.
4. Use UptimeRobot to ping your /health endpoint on the Flask app (if you want an HTTP endpoint kept alive).
