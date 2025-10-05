#!/bin/bash
#(2) Ask the user for a filename, and check if it exists. If it exists, is the file readable and writable.

read -p "Enter the file name: " file 

if [ -e $file ] ; then
	echo "The file $file exists."
	if [ -r $file  ] ; then 
		echo "The file $file is readable "
	else 
		echo "The given file $file is not readable "
	fi 
	
	if [ -w $file ] ; then
		echo "The file $file is writable"
	else 
		echo "The file $file is not writable"
	fi
else 
	echo "The file $file dose not exists."
fi
