# (13) Write a program to concatenate a list of strings to make a sentence using reduce function
from functools import reduce
def conc_list(p,q): return p+q

l1 = ["Hi ", "How ", "Are ", "You "]
concatenate=reduce(conc_list,l1)
print(concatenate)

#or

concatenate2=reduce(lambda x,y:x+y,l1)
print(concatenate2)