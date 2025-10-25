

#a=int(input("enter the number"))
def isprime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
         if n%i==0:
            return False
    return True



#b=isprime(a)
#print(b)