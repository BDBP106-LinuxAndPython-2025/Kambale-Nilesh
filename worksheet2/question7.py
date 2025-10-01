#(7) Write a script to replace all occurrences of a character, c, with another character, d
x=input("Enter the element of the list: ")
y=input("Enter the element which has to be replace: ")
z=input("Enter the element which will replace the element: ")
L=list(x)
a=""
for i in range(len(L)):
    if L[i]==y:
        a+=z
    else:
        a+=L[i]
print(a)