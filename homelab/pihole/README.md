# Set a static IP for the server
- https://docs.pi-hole.net/main/prerequisites/#ip-addressing
- Use the modem/router admin interface to set an IP/DHCP reservation

# Set firewall rules for Pi-hole
So that the server allows incoming queries to Pi-hole ports. Example using `ufw`.
- https://docs.pi-hole.net/main/prerequisites/#ufw
- IPv4:
```
ufw allow 80/tcp
ufw allow 53/tcp
ufw allow 53/udp
ufw allow 67/tcp
ufw allow 67/udp
```
- IPv6:
```
ufw allow 546:547/udp
```

# Install Pi-hole
`curl -sSL https://install.pi-hole.net | bash`

# Set DNS server (optional)
- Use the modem/router admin interface to set the Pi-hole server as the DNS server
- If the Pi-hole server has been set up as the DNS server in the modem, when it is down or disconnects from LAN, all devices in the LAN may **NOT** be able to access internet, because their DNS resolver is not available!
- To avoid this, we can use Wireguard VPN, see below

# Enable remote ssh on the Pi-hole server
- https://linuxize.com/post/how-to-enable-ssh-on-ubuntu-18-04/
- Install openssh: `sudo apt install openssh-server`
- Ask firewall to allow ssh: `sudo ufw allow ssh`
## Only allow key-based authentication on the server (optional)
- https://www.nixcraft.com/t/how-to-only-allow-ssh-key-login-and-disable-passwords/3722
- https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server#step-4-disabling-password-authentication-on-your-server
- Create keys for the client(s) and make sure the client(s) can log in the server using their respective keys first
- Open `sudo nano /etc/ssh/sshd_config`
- Change some settings:
```
PasswordAuthentication no

# These are optional
PermitRootLogin no
PermitRootLogin prohibit-password
```
- Restart ssh
- `sudo systemctl reload sshd.service`
- Or `sudo systemctl restart ssh`
## Forward ssh port from model/router
- Do this to allow ssh to Pi-hole server from outside LAN
- Use the modem/router admin interface to forward a port (e.g., 60022) in router to port 22 in the Pi-hole local IP address
## Try out ssh
- Within LAN:
    - `ssh userName@PiholeIP`
- Use port 60022 if using a DDNS solution:
    - `ssh -p 60022 userName@your_sub_domain.duckdns.org`
- Within Wireguard VPN:
    - `ssh username@PiholeWireguardIP`

# Setup Wireguard to block ads outside network
- https://docs.pi-hole.net/guides/vpn/wireguard/overview/
- Setup wireguard
- Forward a port (e.g., 60023) in router to port 60023 in the Pi-hole local IP
- Set firewall rule so the server allows incoming queries to port 60023:
```
sudo ufw allow 60023/udp
```
- See more in...
    - `wireguard` dir (esp. the DDNS part)
    - `netcheck` dir
- Add some cron jobs to update DDNS of the router and check internet connection periodically:
```
*/5 * * * * /home/userName/duckdns/duck.sh >/dev/null 2>&1
*/5 * * * * /home/userName/freedns/freedns.sh > /dev/null 2>&1
@reboot cd /home/userName/netcheck && yes n | ./netcheck.sh &
```
