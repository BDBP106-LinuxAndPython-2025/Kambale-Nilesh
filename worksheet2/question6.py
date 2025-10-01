# (6) Write a script to find the highest frequency character in a string, S
x=input("Enter the string : ")
L=list(x)
a=0
b=0
for i in L:
    for j in L[::-1]:
        if i==j:
            a+=1
        else:
            b+=1

