#!/bin/bash
# My First Recon Script
# Written by n3o

echo "Starting recon..."
echo "================"

echo "[*] Current User:"
whoami

echo "[*] System Info:"
uname -a

echo "[*] Network Interfaces:"
ip a | grep "inet "

echo "[*] Listening Ports:"
ss -tulnp

echo "[*] Top 5 CPU Processes:"
ps aux --sort=-%cpu | head -6

echo "================"
echo "Recon Complete."

echo "[*] accounts that can login:"
grep ":/bin/bash$" /etc/passwd

echo "[*] Suid Binaries:"
find / -perm -4000 2>/dev/null | head -5

echo "[*] Active Network Connections:"
netstat -an | grep ESTABLISHED
