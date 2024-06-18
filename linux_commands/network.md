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
## Make a query to a specific DNS server
- `nslookup somewhere.com some.dns.server`

# Check resolvectl status
`sudo resolvectl status`

# Set DNS resolvers for an interface
- This will **not** stick after reboot
    - `sudo resolvectl dns interface_name 1.1.1.1 1.0.0.1 8.8.8.8 8.8.4.4`

# Set DNS resolvers globally
- Change `/etc/systemd/resolved.conf` like so:
    ```
    DNS=1.1.1.1 8.8.8.8 9.9.9.11
    FallbackDNS=1.0.0.1 8.8.4.4 149.112.112.11
    ```

# Check behavior of systemd-resolved 
- `sudo resolvectl log-level debug` (default is `info`)
- `journalctl -u systemd-resolved --since "2024-03-26 00:00:00"`

# Check internet connectivity
`wget --spider http://example.com`
