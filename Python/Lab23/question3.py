# (3) Write a Python script to check if a given
# string contains an email address or not.
import re
# a=input("Enter your em@il address: ")
c="255hsbd014@ibab.ac.in"
pattern=r"^[a-z0-9\.\_\%\-]+@[a-z0-9]+[\.a-z]{2,}$"
b=re.fullmatch(pattern,c,re.IGNORECASE)
print(b)
if b:
    print("Your email id is in valid format ! ")
else:
    print("It is not a in valid email id ! ")


