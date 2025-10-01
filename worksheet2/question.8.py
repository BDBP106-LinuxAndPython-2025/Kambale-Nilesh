#(8) Write a program to find the sum and average of numbers in a list, L.
x=input("Enter the number of the list: ")
L=list(x)
add=0
for i in L:
    add=add+int(i)
y=len(L)
z=add/y
print(f'the sum of the list is: {add}')
print(f'the average of the list is: {z}')
