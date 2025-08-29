#!/bin/bash

#using -e
echo "Name of file or directory"
read n
if [ -e $n ] ; then
	echo "file or directory exist" 
else 
	echo "file or directory dose not exist "
fi

# -e in if block checks the if file or directorydose exist in present working directory


echo "Files name"
read n
if [ -s $n ] ; then
        echo "file contains some contains"
else
        echo "file dosent contain any thing"
fi


# -s gives the file dose contain something or not 


echo "Files name"
read n
if [ -f $n ] ; then
        echo "file exist"
else
        echo "file dose not exists"
fi
# it checks the pwd dose have the file or not 
