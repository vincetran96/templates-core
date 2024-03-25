#!/bin/bash
set -e
sudo ifconfig tun0 down
sudo killall -SIGINT openvpn
# sudo ip link delete tun0
echo "Done."
