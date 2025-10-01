# (9) Write a program to find the minimum and maximum number in a list, L
x=str(input("Enter the elements of List: "))
L=list(x)
minimum=int(L[0])
maximum=int(L[0])
for i in L:
    if int(i)<minimum:
        minimum=int(i)
    if int(i)>maximum:
        maximum=int(i)
print(f'The minimum element in list is : {minimum}')
print(f'The maximum element in list is : {maximum}')