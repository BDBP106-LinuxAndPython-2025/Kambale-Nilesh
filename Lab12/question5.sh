#!/bin/bash
#
function divide {
 echo $1 $2
	if [ $2 -eq 0 ] ; then
	echo "Division cannot happen due to divisor is 0"
		
	else 
	local quotient=$( echo "scale=2; $1/$2" | bc )
	local remainder=$[ $1%$2 ]

	echo "Number1=" $1
	echo "Number2=" $2
	echo "Quotient=" $quotient
	echo "Remainder=" $remainder
	fi
		
}
div=$(divide $1 $2)
echo $div 
