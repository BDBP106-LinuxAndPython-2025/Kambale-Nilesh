x=input("Enter the string: ")
a=len(x)
c=0
for i in range(a-1):
    if x[i]=="W":
        c+=1
print(c)