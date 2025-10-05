#!/bin/bash
#7) A script that prints the current disk usage, and if the usage is above 80% print a warning message.

u=$(df -h | sort -k5 -n | tail -n 1 | gawk '{print $5}' | sed 's/%/ /')
	echo "$u%"
if [[ $u -gt 80 ]]; then
	echo "Warning! Disk Usage is above 80%"
fi
