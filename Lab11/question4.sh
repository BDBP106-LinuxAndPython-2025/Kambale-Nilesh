#!/bin/bash

#val1=Jayashree
#val2=Nagesh
#if [ $val1 > $val2 ]; then
#echo "$val1 is greater than $val2"
#else
#echo "$val1 is lesser than $val2"
#fi




val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi
# now it dosent intrepreat the val2 to create as a filw now it work as normal string operation 
