#!/bin/bash
#11) In a directory, rename all files with extension .txt to have a prefix old_

read -p "Enter the directory name : " dir 
if [ -d "$dir" ]; then  
	cd "$dir"
	for file in *.txt ;
	do 
		if [ -e "$dir" ]; then
		       mv "$file" "old_$file"
	       else 
			echo "No such file ending with *.txt"
		fi
	done 
else 
	echo "The directory dose not exists!"
fi
