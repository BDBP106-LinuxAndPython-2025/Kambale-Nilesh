x=input("Enter a binary: ")
r=str(x[::-1])
y=0
j=0
for i in r:
    if int(i)==0 or int(i)==1:
     j+=(int(i)*2**y)
     y+=1
    else:
        j="Error invalid binary"
        break
print(j)
# here y variable used for exponient of the 2^y thus every itrartion it will add 1
# j is a variabe used for sum of each itration thus we will get addition of for loop thus
# product will be the decimal form
