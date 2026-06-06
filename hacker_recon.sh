#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
OUTPUT=~/hacking/results/hacker_recon_$DATE.txt
mkdir -p ~/hacking/results

echo "================================" | tee -a $OUTPUT
echo "HACKER RECON — by n3o" | tee -a $OUTPUT
echo "Date: $DATE" | tee -a $OUTPUT
echo "================================" | tee -a $OUTPUT

echo "[*] Current User:" | tee -a $OUTPUT
whoami | tee -a $OUTPUT

echo "[*] Location:" | tee -a $OUTPUT
pwd | tee -a $OUTPUT

echo "[*] System Info:" | tee -a $OUTPUT
uname -a | tee -a $OUTPUT

echo "[*] User ID & Groups:" | tee -a $OUTPUT
id | tee -a $OUTPUT

echo "[*] Network Location:" | tee -a $OUTPUT
ip a | grep "inet " | tee -a $OUTPUT

echo "[*] Open Ports:" | tee -a $OUTPUT
ss -tulnp | tee -a $OUTPUT

echo "[*] Active Connections:" | tee -a $OUTPUT
netstat -an | grep ESTABLISHED | tee -a $OUTPUT

echo "[*] Top CPU Processes:" | tee -a $OUTPUT
ps aux --sort=-%cpu | head -10 | tee -a $OUTPUT

echo "[*] SUID Binaries:" | tee -a $OUTPUT
find / -perm -4000 2>/dev/null | tee -a $OUTPUT

echo "[*] Login Accounts:" | tee -a $OUTPUT
cat /etc/passwd | cut -d: -f1,7 | grep ":/bin/bash$" | tee -a $OUTPUT

echo "================================" | tee -a $OUTPUT
echo "Recon complete. Saved to: $OUTPUT" | tee -a $OUTPUT
