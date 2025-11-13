#!/bin/bash
device="/dev/sda"
if [ ! -e "$device" ]; then
  echo "Device $device does not exist."
  exit 1
fi
partition="/dev/sda3"
number_partition=3
current_size=$(fdisk -l "$device" | grep "$partition" | awk '{print $5}')
start_sector=$(fdisk -l "$device" | grep "$partition" | awk '{print $2}')
sudo fdisk "$device" <<EOF
d
$number_partition
n
p
3
$start_sector

w
EOF
sudo partprobe /dev/sda
sudo pvs
sudo pvresize /dev/sda3
sudo pvs
sudo pvresize /dev/sda3
sudo lvextend -r -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo reboot now

