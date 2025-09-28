x=input("Enter the string: ")
a=len(x)
c=""
d=""
for i in range(0,a,2):
    c+=(x[i])
print(c)
for i in range(1,a,2):
    d+=(x[i])
print(d)