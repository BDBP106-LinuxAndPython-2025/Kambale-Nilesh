#!/bin/bash

#(3) A script that counts the number of words, lines and characters in a given text file.

read -p "Enter the name of the file: " file 

if [[ -f $file  ]]; then 
	echo "Number of words contain in file:" `wc $file`
else
	echo "File dose not exists!"
fi 
