#!/bin/bash

read n
a=1
until [ $a -gt 15 ]
do 
	b=$[n*a]
	echo "$a x $n =" $b
	a=$[a+1]
done


