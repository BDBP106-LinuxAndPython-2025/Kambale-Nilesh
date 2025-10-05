#!/bin/bash
#5) A script that takes a word and a filename, then prints the lines where the word appears.
read -p "Enter the word : " w
read -p "Enter the file name : " f 
if [ -f "$f" ]; then 	
	if   grep -n "$w" "$f" ; then
	      echo "Only these matches found for the word $w "
      			      
	else 
		echo "No match found or file dose not contaion such word" 
	fi
else 
	echo "File dose not exists!"
fi

