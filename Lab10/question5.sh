#!/bin/bash

read n
echo "For The Number "$n


if [ "$n" -gt 0 ]; then
        echo "Your Number "$n" Is a Positive Number"
elif [ "$n" -lt 0 ]; then
        echo "Your Number "$n" Is a Negative Number"
else 
        echo "Your Number "$n" It is Zero"
fi

