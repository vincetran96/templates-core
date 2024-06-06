# Start tailscale
- `tailscale up --accept-dns=true` (with MagicDNS)
- `tailscale up --accept-dns=false` (without MagicDNS)

# Set up a subnet router
- So devices can see each other as in a local network (?)
- https://tailscale.com/kb/1019/subnets/?tab=linux
- `tailscale up --accept-dns=false --advertise-routes=192.168.1.0/24`

# Tailscale and DNS
- https://tailscale.com/kb/1188/linux-dns

# Tailscale ping another node
`tailscale ping --verbose=true nodename`
