#!/bin/bash

echo "The value  of vairable $HOME"

val1=23934
val2=44343
val3=$(bc << EOF
scale=5
x1=($val1/$val2)
x1*1
EOF
)
echo "calculation  "$val3

echo `ls /home/ibab | grep "D"`
echo `cat /etc/passwd | grep "ibab" `                               
