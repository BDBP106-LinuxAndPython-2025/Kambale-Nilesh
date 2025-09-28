x=str(input("Enter thr elemnts of list : "))
k=str(input("Enter thr elemnt need to be removed : "))
L=[] # creation of list
for i in x:
    L.append(i)
for i in L:
    if i==k:
        L.remove(i)
print (f'The list after removing {k} elements is : {L}')



