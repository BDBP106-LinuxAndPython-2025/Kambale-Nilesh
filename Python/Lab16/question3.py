N=int(input("Enter the number "))
a="prime"
if N==0:
    a="Not prime"
else:

    for i in range(2,N):
        if  N%i==0:
            a="Not prime"
            break
        else :
            a="prime"
print (f"{N} is {a} number")









