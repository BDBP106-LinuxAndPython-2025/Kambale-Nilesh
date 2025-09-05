#!/bin/bash


#Q3 sorting dat according to height column

sort -t ',' -k2 -n SOCR-HeightWeight.csv
#this command will sort data according to column 2  -t seprate fields ',' is field seprator -n for numeric sort
# so answer is index 1894 having height 75.528 invches & weight 146.9701 in pound
# then we will check for how column 3 which is 3 rd column for weight in pound
sort -t ',' -k3 -n SOCR-HeightWeight.csv
# so answer for this question is no tallest person dose not weight the most the most weighted person is index 10235 having height 70.71 inches & weight 170.124 pound 

