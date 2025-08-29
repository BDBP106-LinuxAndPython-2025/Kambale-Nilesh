#!/bin/bash

read -ra numbers < nums.txt 

echo "${numbers[@]}"

for n in "${numbers[@]}"
do 
	double=$((n*2))
	echo "$n double = $double"
done
