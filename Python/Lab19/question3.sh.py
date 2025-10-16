#3) Write a program to convert a tuple of angles into a list of tuples with each tuple containing the sine and cosine of an angle

a=tuple(map(int, input("Enter the angles in degrees: ").split()))
import math
s=[math.sin(math.radians(i)) for i in a]
c=[math.cos(math.radians(i)) for i in a]
h=[(a[i],s[i],c[i]) for i in range(len(a))]
print("For the given angles the value (angle,sin,cos) :", h)




