#!/bin/bash

read b
a=1
while  [ $a -lt 16 ]
do 
	y=$[b*a]
	echo "$b x $a ="$y
	a=$[a+1]
done
