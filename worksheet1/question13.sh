#!/bin/bash
#(13) Display a menu with options: 1) Show date, 2) Show calendar, 3) show logged-in users,
#4) Exit. The script should display these options, execute the appropriate command according to the option
echo "====Options====="
echo 
echo "1) Show Date"
echo "2) Show Calender"
echo "3) Show Logged-in Users"
echo "4) Exit"
echo
read -p "Give any suitable option: " o
if [ "$o" -eq 1 ]; then
	date 
elif [ "$o" -eq 2 ]; then
	echo "`cal`"
elif [ "$o" -eq 3 ]; then
	who
elif [ "$o" -eq 4 ]; then
	echo "Exit"
else 
	echo "Choose valid option between 1-4"	
fi
echo "======End======"
