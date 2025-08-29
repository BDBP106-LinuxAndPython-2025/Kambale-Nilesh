#!/bin/bash

function directory {
	local check=$1
	if [ -d "$check" ]; then
		echo "Directory alredy exist"
        ls 
	else
		echo "Directory dosent exist thus creating new one"
		mkdir $check	
	fi
}
directory "$1"
