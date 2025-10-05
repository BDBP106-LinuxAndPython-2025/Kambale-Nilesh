#!/bin/bash
# 9) Create an array of 5 numbers. The script should print the largest number, smallest
# number and sum of all numbers in the array.
arr=(67 94 403 22 727 23)
max=0
for i in "${arr[@]}"
do
	if [ "$max" -lt "$i" ]; then
		max=$i
	fi
done
echo "The maximum number is:" $max

min=${arr[0]}
for i in "${arr[@]}"
do
	if [ "$min" -gt "$i" ]; then
		min=$i
	fi
done
echo "The minimum number is:" $min

sum=0
for i in ${arr[@]}
do
	sum=$[ $sum+$i ]
done
echo "The sum of numbers is:" $sum
