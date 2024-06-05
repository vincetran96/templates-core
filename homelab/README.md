# What is this folder? For homelab/home server stuff
- Computer hierarchy (from root)
- Manpages
- FAQs (links from external resources)
- Tailscale
- Pi-hole
- Wireguard VPN
- Netcheck
- Caddy
- Nextcloud

# Access homelab server
## Using tailscale
`ssh username@homelab_tailscale_name -i ~/.ssh/homelab_name.id_rsa`

## Using public DNS name
`ssh username@homelab_dns_name.dedyn.io -i ~/.ssh/homelab_name.id_rsa -p ssh_port`

# Net
## Check current DNS server in-use
`cat /etc/resolv.conf `
## Check DNS servers for each interface
`resolvectl status`
## Check DNS speed
- https://www.baeldung.com/linux/dns-speed-test
## systemd-resolved and NetworkManager
- https://sites.google.com/site/nandydandyoracle/orabuntu-lxc/using-systemd-resolved-in-a-networkmanager-environment
