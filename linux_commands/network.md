# Check what things are listening
- `sudo lsof -i -P -n | grep LISTEN`
- `sudo netstat -tulpn | grep LISTEN`
- `sudo ss -tulpn | grep LISTEN`

# Check my DNS settings
`cat /etc/resolv.conf`

# Lookup IP of DNS name in current DNS server
- `nslookup internal.host.com`
- `resolvectl query internal.host.com`
## Per-interface query
- `resolvectl query example.com -i interface_name`

# Check resolvectl status
`sudo resolvectl status`

# Check behavior of systemd-resolved 
- `sudo resolvectl log-level debug` (default is `info`)
- `journalctl -u systemd-resolved --since "2024-03-26 00:00:00"`

# Check internet connectivity
`wget --spider http://example.com`
