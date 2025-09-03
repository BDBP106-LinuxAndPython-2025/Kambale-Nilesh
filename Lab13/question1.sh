#!/bin/bash
# 1) Create a text file containing the following text and do the following actions using sed



#(i) Print only the lines where the word and appears.
echo "answer for (i)"
sed -n '/and/p' file.txt
echo""
#(ii) Change all instances of the word ’language’ into ‘lang’.
echo "answer for (ii)"
sed 's/language/lang/' file.txt
echo""
#(iii) Delete lines containing the word ‘is’.
echo "answer for (iii)"
sed '/is/d' file.txt
echo""

#(iv) Find a way to insert line numbers at the beginning of each line
echo "answer for (iv)"
sed '=' file.txt | sed 'N;s/\n//'
echo""

#(v) Remove 1st 2 lines only
echo "answer for (v)"
sed '1,2d' file.txt
echo""

#(vi) Find a way to print every other line in the above file.
echo "answer for (vi)"
sed -n 'p;n' file.txt
echo""
# -n supress automatic printing of each line but cannot work without processing the command 'p;n' this line, in 'p;n' comand  p  will print current line  n afeter p skipp next line 

#(vii) Substitute first instance of ‘Python’ by ‘python’ and ‘language’ into ‘lang’ using
echo "answer for (vii)"
sed '0,/Python/s/Python/python/;0,/language/s/language/lang/' file.txt

