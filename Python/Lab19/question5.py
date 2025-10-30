# (5) Write a program to find the sum of all the elements in a list using lambda and reduce
# functions.
l=[1,2,3,4,5,6,7,8,9]
from functools import reduce
def sum1(x,y) :return x+y
sum_using_reduce=reduce(sum1,l)
print(sum_using_reduce)

sum_using_lambda=reduce(lambda x,y:x+y,l)
print(sum_using_lambda)