# (2) Creating your own package. Create a package (folder) called utils with an empty
# __init__.py. Inside utils create two python files called math_utils.py and string_utils.py.
# The former should contain functions to perform operations such as addition, subtraction,
# multiplication, division and getting remainder with two numbers as inputs. The latter file
# should contain functions to convert lower case to upper case, upper case to lower case and
# to concatenate strings. In a different program, import math_utils and string_utils to
# use the modules to print the output for the following: a) 34 and 45, b) ’BDBH’ and ’101’.


import utils.math_utils

x=utils.math_utils.add(34,45)
print(x)
y=utils.math_utils.sub(34,45)
print(y)
z=utils.math_utils.mul(34,45)
print(z)
w=utils.math_utils.div(34,45)
print(w)

import utils.string_utils
q=utils.string_utils.lower("BDBH")
print(q)
q=utils.string_utils.upper("bdbh")
print(q)
r=utils.string_utils.concat("BDBH","101")
print(r)
