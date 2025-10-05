#!/bin/bash
#(6) A script to generate the multiplication table for a given number from 1 to 20.
read -p "Enter the number : " n
if  [ $n -gt 0 ]; then
	for i in {1..20}; do
  	 	echo "$n x $i = $((n * i))"
	done
else 
	echo "Given number is less than 1 "
fi
