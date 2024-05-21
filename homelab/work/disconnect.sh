#!/bin/bash
set -e
sudo ip link delete tun0
sudo killall -SIGINT openvpn
echo "Done."
