#!/bin/bash
# Getting the username of the logged-in user
logged_in_user=$(whoami)
# Checking if the user is logged in
if [ -n "$logged_in_user" ]; then

echo "The logged-in user is: $logged_in_user"
else
echo "User is not logged in"
fi

# after if statment in evaluation parantheses block logged_in_user vairable was not proper missing "g"
# opening perantheses bracket was not same as closing [) it should be like [] or (()) 
# semi ; colon was missing after brackets 
# in echo command _ was missing in command insted - was in logged_in_user vairable % user was in Capital Case 
