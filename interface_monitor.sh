#! /bin/bash

read -p "Enter a interface name" INT

airmon-ng check kill
sudo ip link set $INT down
sudo iw dev $INT set type monitor
sudo ip link set $INT up
sudo ip link show $INT
