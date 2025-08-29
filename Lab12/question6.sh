#!/bin/bash

function maximum {
           local num1=$1 
	   local num2=$2
  if [ $num1 -gt $num2 ] ; then
	echo " maximum is "$num1
 else 
	echo " maximum is "$num2
 fi
}
maximum "$1" "$2"
