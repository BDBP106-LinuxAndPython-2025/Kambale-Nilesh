#!/bin/bash
#12) A script that prints the current time only every 10 seconds for a minute.

for i in {1..6}; do
	echo $(date +"%T")
	sleep 10
done
