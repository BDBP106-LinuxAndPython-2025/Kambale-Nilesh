#1/bin/bash
# checking if a file exists
#
filename=$1
if [ -f "$filename" ] ; then
        echo "The File Name '$1' Dose exists!" 
else
        echo "The File '$1' Does Not exists!" 
fi
#Checking If The  File is Executable or Not 
if [ -x "$filename" ] ; then
        echo "The file '$1' is executable!"
else
        echo "The File '$1' is not executable!"
fi
