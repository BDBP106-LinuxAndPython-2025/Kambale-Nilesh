#!/bin/bash

ls
# lists the file in present woking directory
ls > listoffiles
# it creates a file & saves the out put of ls in this file
ls 1> listoffiles





ls -l . newdir
# ls cannot such file or directory in present working directory  while ls -l give full details of files & directories
ls -l . newdir 1>presentfile 2>filesnotpresent
# the file presentfile store out put of functiob ls -l & the file filesnotpresent stores newdir erro output respectively thus numbes before ">" sign dictates which output to be stored

#ii)
ls -l . newdir >listoffiles 
# now this file contains the out put of ls -l 

