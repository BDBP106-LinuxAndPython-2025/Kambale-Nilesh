#(7) Write a program with a function to find whether a given triangle with sides a, b, c is
# isosceles, scalene or equilateral triangle, also provide a test case output from the program.
x=input("Enter the value of side of trangle (give input in spaces): ").split()
l=list(map(int,x))
import math
def triangle(a,b,c):
    if a==b==c:
        print("The triangle is equilateral")
    elif a==b or a==c or b==c or c==a:
        print("The triangle is isosceles")
    else :
        print("The triangle is scalene")
triangle(l[0],l[1],l[2])

