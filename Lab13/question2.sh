#!/bin/bash

#(i) Find a way to print the people’names who are scored less than 25 in their subjects.
echo "Answer 0f (i)"
gawk '{if ($2<25) print $1}' gawk.txt
echo""
#(ii) Print the student whose Physics score is given.
echo "Answer of (ii)"
gawk '{if ($2==26) print $1}' gawk.txt
echo""

#(iii) Find a way to rewrite the data into a csv format in a new file called data2.csv
echo "text data added to data.csv"
gawk '{print $0}' gawk.txt > data.csv

