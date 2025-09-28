x=str(input("Enter elements of list: "))
L=[]
for i in x:
    L.append(i)
L2=[] # creation of second list for storing seen elemrnts
L3=[] # creation of third list for storing duplicate elements
for i in L:
    if i in L2:
        if i not in L3:
            L3.append(i)
    else:
        L2.append(i)
if not L3:
    print("No duplicate elements seen")
else:
    print(f'The duplicate elements are {L3}')

