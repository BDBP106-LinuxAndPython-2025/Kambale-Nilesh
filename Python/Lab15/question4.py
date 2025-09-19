angle=int(input("Enter an angle in degrees="))
import math
a = math.radians(angle)
print (f"Radian equvivalent is ", {a})
b=math.sin(a)
c=math.cos(a)
d=math.tan(a)
se=(1/c)
ct=(1/d)
csc=(1/b)
print ( f"value of sin", {b} )
print ( f"value of cos", {c} )
print ( f"value of tan", {d} )
print ( f"value of sec", {se} )
print ( f"value of cot", {ct} )
print ( f"value of cosec",{csc} )


