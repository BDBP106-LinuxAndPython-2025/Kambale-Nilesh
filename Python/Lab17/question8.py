#(8) Write a program to interchange the even and odd components of an input list. The list
# can contain any type of variables. Output the result for the following example:

a=[23,32,33,44,'BDBH101','hello','python', 15, 1e-10, True,'hit']
b=[]
for i in range(len(a)):
      if i %2==0:
          temp=a[i]
      else:
          b.append(a[i])
          b.append(temp)
print(b)
