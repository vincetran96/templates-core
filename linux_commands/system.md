# Resources
- https://linuxhandbook.com/check-if-systemd/
- https://askubuntu.com/questions/1031439/am-i-running-networkmanager-or-networkd

# Check if system is running on systemd
`ps -p 1 -o comm=`

# Journalctl
- `journalctl -u systemd-resolved --since "2024-03-26 00:00:00"`
- `journalctl -u systemd-resolved --since "10min ago"`
