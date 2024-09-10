#!/bin/bash

systemctl stop clamav-freshclam
rm -rf /var/lib/clamav/*

wget http://94.247.111.11/clamav/main.cvd -O /var/lib/clamav/main.cvd 
wget http://94.247.111.11/clamav/daily.cvd -O /var/lib/clamav/daily.cvd 
wget http://94.247.111.11/clamav/bytecode.cvd -O /var/lib/clamav/bytecode.cvd

# Устанавливаем крон для ежедневного обновления баз
echo "0 2 * * 6  /opt/update_clamav.sh" | crontab -