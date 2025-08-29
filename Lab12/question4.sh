#!/bin/bash

read -ra numbers < nums.txt 

echo "${number[@]}"

for n in "${number[@]}"
do 
	double=$((n*2))
	echo "$N double = $double"
done
