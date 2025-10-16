#(2) Lists and do loops
#(i) Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
a=[i for i in range(1, 51)]
s=sum([ i for i in a ])
print(s)

#(ii) Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b=[x for x in range(2, 52) if sum(1 for i in range(2, x) if x % i == 0) == 0]
print(b)

#(iii) Using a do loop structure, collect all the common numbers in a and b into a new list c.
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)

#d=[ i for i in a  for j in b if i==j ]
#print(d)