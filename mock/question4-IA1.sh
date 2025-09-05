#!/bin/bash
read=$1 

IFS=$'\n' 
while $( read )

do
	echo $read
done

#IFS internal fileld seprator ,\n
