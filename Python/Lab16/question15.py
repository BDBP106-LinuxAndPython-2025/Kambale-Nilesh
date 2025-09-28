x=input("Enter the string: ").split()
y=input("Enter the charcter the word which stating with(k): ")
L=list(x)
L2=[]
for ch in L:
    if ch.startswith(y):
        L2.append(ch)
print(f'The list after extracting the word starting with ({y}) :{L2}')






