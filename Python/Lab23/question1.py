# (1) Write a regular expression that accepting a 3-digit integer between 000 and 255. Imple-
# ment this in a script and test it for various possibilities

import re
a=input("Enter a three digit number: ")
pattern=r"(^[01]\d{2}|2[0-4][0-9]|25[0-5])$"
b=re.match(pattern,a)
print(b)
if b:
    print("Yes given integer is 3 digit between 000-255, Match Found ! ")
else:
    print("No given integer is not in required format between 000-255")
