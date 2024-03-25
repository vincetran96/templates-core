#!/bin/bash
cd /home/username/work/Company/staff-vpn-2025
sudo openvpn --config staff_ca_2025.ovpn --auth-user-pass /home/username/work/Company/ldap &
while true; do
    if ifconfig "tun0" >/dev/null 2>&1; then
        echo "Network interface tun0 is available."
        break
    else
        echo "Network interface tun0 is not available. Retrying..."
        sleep 3
    fi
done
sleep 3
echo "Done."
