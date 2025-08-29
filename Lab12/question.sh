#!/bin/bash
#
n=$1
until [ "$n" -gt 15 ]
b=1
do 
	echo $n
	n=$[$1*$b]
       	b=$[b+1]
done


