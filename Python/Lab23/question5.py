# (5) Write a Python script that scans through a given piece of text and extracts all unique
# email addresses from it.
import re
pattern = r"[a-z0-9\.\-\%\_]+@[a-z0-9\.\_]+\.[a-z]{2,}"
mails =" 255hsbd014@ibab.ac.in,234@ibab.ac.in ,255habd014@ibab.ac.in,255habd000@ibab.ac.in,255habd014@ibab.ac.in"
uni = set(re.findall(pattern,mails))
print(uni)


