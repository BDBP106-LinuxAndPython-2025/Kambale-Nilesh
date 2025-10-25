# (2) Write a regular expression that matches integers from 0 to 255. (Note that this is different
# from the q
import re
a=input("Enter a three digit number: ")
pattern=r"(^\d|\d\d|[01]\d{2}|2[0-4][0-9]|25[0-5])$"
b=re.match(pattern,a)
print(b)
if b:
    print("Yes given integer is 3 digit between 000-255, Match Found ! ")
else:
    print("No given integer is not in required format between 000-255")