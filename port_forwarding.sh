#!/bin/bash
set -x
sudo sysctl net.ipv4.ip_forward=1
echo $(ifconfig enp1s0 | grep "inet " | awk -F'[: ]+' '{ print $4 }')
sudo iptables -t nat -A PREROUTING -p tcp -d $(ifconfig enp1s0 | grep "inet " | awk -F'[: ]+' '{ print $4 }') --dport 8089 -j DNAT --to-destination 192.168.1.1:8088
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
