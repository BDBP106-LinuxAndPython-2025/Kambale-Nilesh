#!/bin/bash



# for evaluation of mock test dont consider this beacuse this one is solved after the crossing 4:30 time limit 

n=$#
if [ $n -eq 4 ]; then
	echo " The four arguments are = $@ "
	exit 0
else
	echo " For these 4 arguments are required "
	exit 1
fi
