# (11) A magic date is a date where the date multiplied by the month is equal to the two-digit
# year. For example, June 10, 1960 is a magic date because June is the sixth month, and
# 6 times 10 is 60 which is the two-digit year. Write a function that determines whether
# or not a date is a magic date. Use your function to create a main program that finds
# and displays all of the magic dates in the 20th century.
x=input("Enter the date includes space as sepration chracter,ex.(10 5 2020) : ").split()
l=list(map(int,x))

s=list(x[2])
d= str(s[2]) + str(s[3])
#print(d)
if l[0]*l[1] == int(d) :
    print("The given date is magical date" )
else :
    print("The given date is not magical date")
L1=[] # creation of list for month
for i in range(1,13):
    L1.append(i)
L2=[] # creation of list for day
for i in range(1,31):
    L2.append(i)
L3=[] # creation of list for year
for i in range(1901,2002):
    L3.append(i)
def magical_date(a, b, c):
    l4=[]
    for i in a:
        for j in b:
            for k in c:
                if i*j == (k%100):
                    f=f"{i} {j} {k}"
                    l4.append(f)

    return l4
result=magical_date(L1, L2, L3)
print(result)