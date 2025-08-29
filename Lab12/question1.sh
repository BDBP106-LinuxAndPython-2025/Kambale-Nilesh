#!/bin/bash

n=1
# until
until [ "$n" -eq 11 ]
do
	echo $n
	n=$[$n+1]
done

