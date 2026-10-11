#!/bin/bash
while true; do
	echo "1. Display human-readable disk usage"
	echo "2. Display free and used memory"
	echo "3. Display system uptime and current load average"
	echo "4. Display active network interface and their IP address"
	echo "5. Exit"
	read -p "Enter your choice -" ch
	case $ch in
		1)
			df -h
			;;
		2)
			free -h
			;;
		3)
			uptime
			;;
		4)
			ifconfig
			;;
		5)
			exit 0
			;;
		*)
			echo "Incorrect option"
			;;
	esac
done
