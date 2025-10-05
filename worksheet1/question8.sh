#!/bin/bash
#(8) A script that prints a mini-system report that includes a) current date and time, b)
#logged-in users, c) system uptime and d) top 5 processes by memory usage.

echo "======== Mini-System Report ======== "
echo 
echo "a) current date & time              : " `date` 
echo
echo "b) logged-in users                  : " `who`
echo
echo "c) system uptime                    : " `uptime`
echo 
echo "d) Top 5 processes by memory usage  : " 
echo "USER|PID|%CPU|%MEM|VSZ|RSS|TTY|STAT|START|TIME|"
echo "`ps aux | sort -k4 -n | tail -5 | awk '{print $1,$2,$3,$4,$5,$6,$7,$8,$9}' | sort -nr`"
echo "=============== End ================ "
