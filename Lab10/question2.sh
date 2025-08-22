#!/bin/bash

echo "Input a Number: "
read n
echo "I read the number "$n


if [ "$n" -gt 18 ]; then
        echo "Your are an adult"
else
        echo "Your are a minor"
fi

