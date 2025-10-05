#!/bin/bash
# 1) The script should take an integer input and check if it is prime or not

echo "Enter the number:"
read a

if (( $a<=1 )); then
	echo "Given number is not prime"
	exit 
fi 

if (( $a%2 == 0 )); then
	echo "Given number is not prime"
	exit 
fi

i=3
while (( i*i<= $a )); do 
	if (( $a%i==0 )); then
		echo "Given number is not prime"
		exit 

	fi 
	(( i +=2 ))
done

echo "Given number is prime"
