x=str(input("Enter elements of list: "))
k=int(input("Enter the number of times element appered (k): "))
L=[]
L2=[]
L3=[]
for i in x:
    L.append(int(i))
for i in L:
    if L.count(i)>=k:
        L2.append(i)
        if i not in L3:
            L3.append(i)
if not L3:
    print("No such element found")
else:
    print(f'The Elemets appered k times in list : {L3}')