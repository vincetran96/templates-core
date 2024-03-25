# Check what things are listening
`lsof -i -P -n | grep LISTEN`

# Check my DNS settings
`cat /etc/resolv.conf`

# Lookup IP of DNS name in current DNS server
`nslookup internal.host.com`

# Check resolvectl status (on systems running `systemd`)
`sudo resolvectl status`
