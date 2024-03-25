For homelab/home server stuff
- Pi-hole
- Wireguard VPN
- Netcheck

# Access homelab server
## Using tailscale
`ssh username@homelab_tailscale_name -i ~/.ssh/homelab_name.id_rsa`

## Using public DNS name
`ssh username@homelab_dns_name.dedyn.io -i ~/.ssh/homelab_name.id_rsa -p ssh_port`

# Net
## Check current DNS server in-use
`cat /etc/resolv.conf `
