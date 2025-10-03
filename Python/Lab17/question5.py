#(5) Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the
#set() function might be useful here.)
x=input("Enter the string : ").split()
z=set(x)
y=" ".join(z)
print(y)