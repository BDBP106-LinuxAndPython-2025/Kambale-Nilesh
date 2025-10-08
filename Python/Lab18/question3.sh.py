# (3) List comprehension with strings Use list comprehension technique you learnt in class to do the following
# (i) Using the join method.
# (a) Create a string by joining the numbers in the above list a using the comma.
l=[i for i in range(1, 51)]
a=[','.join([ str(i) for i in l])]
print(a)

# (b) Create a string by joining the numbers in the above list a using the period.
b=['.'.join([ str(i) for i in l ])]
print(b)

# (c) Create a string by joining the numbers in the above list a using the ‘—’.
c=['_'.join([ str(i) for i in l ])]
print(c)

# (d) Create a new string by first creating a list of squares of the elements in a,
# then listing them alongside the elements of a line by line. In other words,
# we want a data set that looks like
# 11
# 24
# 39
# ...
d='\n'.join([f"{i} {i*i}" for i in l])
print(d)

#(ii) Make a list of 10 people you know, and do the following:

# (a) Convert each element in the list to upper case using list comprehension
names=["Nilesh kambale", "Atharva kadam", "Sanket koli", "Keshav pande", "Nikhil rana", "Arpit kambe", "Hemad bhoyar", "Satish vankhede","Sandesh, joshi"]
a=[name.upper() for name in names ]
print(a)

# (b) Swap the first name and surname of each element in the list
b=[' '.join(name.split()[::-1]) for name in names]
print(b)

# (c) Join the first name and surname in each element as ’First.Last’. Note that
# the first letter of the first name and first letter of the surname should be
# upper case.
c=[f'{name.split()[0].capitalize()} {name.split()[1].capitalize()}' for name in names ]
print(c)

#(iii) Find the longest word in this sentence using list comprehension: ”She sells sea shells that she collects from the sea floor”.
comp="She sells sea shells that she collects from the sea floor"
words=comp.split()
long=[i for i in words if len(i)==max(len(i) for i in words) ]
print(long)

#(iv) Create a list of the words that are repeated in the above sentence.
repeated=[i for i in words if words.count(i)>1]
print(repeated)

