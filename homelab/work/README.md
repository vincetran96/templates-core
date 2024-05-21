# Setup
## OVPN
```
mkdir -p Company/staff-vpn-2025
cp connect.sh disconnect.sh fix-resolved-route-up.sh fix-resolved-route-pre-down.sh Company/staff-vpn-2025/
```
Optional:
- Replace the text `Company` with your actual company name: `sed -i 's/Company/COMPANY_NAME/g' connect.sh`
- Replace the text `username` with your actual username: `sed -i 's/username/USERNAME/g' connect.sh`

# Connect/Disconnect to work VPN
- `sudo /home/username/work/Company/staff-vpn-2025/connect.sh`
- `sudo /home/username/work/Company/staff-vpn-2025/disconnect.sh`

## LDAP
Replace your username and password in the `ldap` file

# Resources
## General VPN and OpenVPN issues
- https://www.learnitguide.net/2023/04/how-do-i-check-my-dns-settings-in-linux.html
- https://askubuntu.com/questions/1247326/problem-with-dns-with-openvpn-on-ubuntu-20-04
- https://askubuntu.com/questions/298419/how-to-disconnect-from-openvpn
- https://forums.openvpn.net/viewtopic.php?t=36914

## `resolved` issues
- https://askubuntu.com/questions/907246/how-to-disable-systemd-resolved-in-ubuntu
