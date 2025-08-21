#!/bin/bash

echo "Energy = Mass(m) * Speed(s)"
energy=$(bc << EOF
scale =5
m=1
s=(3*(10^8))
m*(s)^2
EOF
)
echo "Energy of an object is "$energy joules
