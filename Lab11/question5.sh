#!/bin/bash


var1="Testing"
var2="testing"
if [ $var1 \> $var2 ];then
	echo "$var1 is greater than $var2"
else
	echo "$var2 is greater than $var1"
fi


#Output = "testing is greater than Testing"The shell intrepreates the testing which is $var2 as Grater vairable "

#After the sort command  "testing" and then "Testing" results as "testing" < "Testing" different than if where as it intrepreats as  "testing" > "Testing"

#Thus, "if" command handles upper and lower cases just opposite to the way "sort" command handles upper and lower cases.


