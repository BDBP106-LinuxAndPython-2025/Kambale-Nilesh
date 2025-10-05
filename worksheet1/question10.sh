#!/bin/bash
#10) A script that takes a .csv file and prints only the first and third columns

echo "Enter a csv format file name : "
read f

if [[ "$f" != *.csv ]]; then
	echo "File Error! (Enter a valid .csv file)"
else
        gawk -F, '{print $1,$3}' "$f"
fi
