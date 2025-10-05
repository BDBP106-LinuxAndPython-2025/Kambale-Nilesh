#!/bin/bash
#(4) List the contents of the current directory and also the name and size of the largest file.
echo "The contents of current directory are : "
echo `ls`
ls -lh | head -n 2 | tail -n1 | awk `{ print $9, $5 }`
