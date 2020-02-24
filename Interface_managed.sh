#! /bin/bash

read -p "Enter a interface name" INT


sudo ip link set $INT down
sudo iw dev $INT set type managed
sudo ip link set $INT up
sudo ip link show $INT
service network-manager restart
