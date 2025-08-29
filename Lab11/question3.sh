#!/bin/bash

# -n to check the string is empty or not 
echo Input the string  
read n
if [ -n "$n" ] ; then
        echo "The string is not empty!" 
else
        echo "The String is empty!" 
fi

# -n to check the string is empty or not
echo Input the string
read n
if [ -z "$n" ] ; then
        echo "The string is empty"
else
        echo "The String is not empty!"
fi

# for -n ; for value of string  , if string is not empty it will execute the if statement " if string is empty it will execute else statment " the string is  empty
# for -z it's check the the if string is empty thus, for the case string is empty it will execute "if"statement otherwise "else" statement it has logic opposite to the -n  

