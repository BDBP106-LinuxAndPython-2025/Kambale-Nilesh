#!/bin/bash
#

echo "Input a number: "
read n
if [ "$n" -gt 100 ]; then
       echo "The number is greater than 100."
elif [ "$n" = 100 ]; then
     echo "The number is equal to 100."

else  
     echo "The number is lesser than 100."
fi




#the bracket should be"[]" like that or "(()) but for this bracket we cannot use "= " insted we use "==" or "-eq2" "
# We dont need another if llop in single loop it can be done
# dont miss the ";" after some argument in if ,elif ,else or  loop for then block
# if statment will chech the number is greter than 100 or not,
#elif block for the number is equal to 100 or not then not else echo as negatve 
#
