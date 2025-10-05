#!/bin/bash
#14) A script that monitors the memory usage (free -m) for 5 minutes and prints a warning if free memory is below 500MB.

for i in {1..5}
do
	frmem=$(free -m | gawk '/^Mem:/ {print $4}')
	echo "Free Memory available is:" $frmem"MB"
	if [ "$frmem" -lt 500 ]; then
		echo "WARNING! memory is less than 500MB."
	fi
sleep 1m
done
