#1/bin/bash
# checking if a file exists if, it exists so exit 200 , if not then 201
#
filename=$1
if [ -f "$filename" ] ; then
        echo "The File Name '$1' Dose exists!"
        exit 200	
else
        echo "The File '$1' Does Not exists!" 
	exit 201
fi
# Q4(i) To Check The Exit Code Is Genrated Or Not In Terminal Command Line Just Type echo $?.


if [ -f "$filename" ] ; then
	echo $?
        echo "The File Name '$1' Dose exists!"
        exit 200
else
        echo "The File '$1' Does Not exists!" 
        exit 201
fi
# Q4(ii) If We Added The echo $? Command After The If The loop does't Interpreat the echo$?.   


if [ -f "$filename" ] ; then
        echo $?
        echo "The File Name '$1' Dose exists!"
        exit 200
else
        echo "The File '$1' Does Not exists!"
        exit 201
fi
# Q4(iii) If We Added The echo $? Before The exit in Shell The loop Does't Interpreat The echo$?. the only one case the echo$? command work if it is added in saprete line without any loop 
