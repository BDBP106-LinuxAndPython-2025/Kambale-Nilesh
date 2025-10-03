#6)Write a program with a function to calculate the area of a triangle using the formula,
# where a,b,c are sides of the triangle, also providing a test case output from the program
# Area= s(s − a)(s − b)(s − c) where 2s = a + b + c
x=input("Enter the value of side of trangle: ").split()
l=list(map(int,x))
import cmath
def area(a,b,c):
    s=(a+b+c)/2
    print(cmath.sqrt(s*(s-a)*(s-b)*(s-c)).real)
if  len(l) == 3 :
    area(l[0],l[1],l[2])
else :
    print("Give the valid side of triangles")