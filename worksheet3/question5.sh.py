# #(5) Write functions to add and subtract two matrices of m× n. Below these two functions,
# create two example matrices that have the same dimensions (rows and columns) and
# therefore correctly does the addition and subtraction Also come up with an example
# where the addition and subtraction are not defined, and hence the runtime errors show
# up.
def addition(m,n):
    if len(m)!=len(n) or len(m[0])!=len(n[0]):
        raise ValueError(".")
    result=[]
    for j in range(len(m)):
        row=[]
        for i in range(len(m[0])):
            row.append(m[j][i] + n[j][i])
        result.append(row)
    return result

def subtract(m,n):
    if len(m)!=len(n) or len(m[0])!=len(n[0]):
        raise ValueError("The matrices should have the same dimensions.")

    result=[]
    for j in range(len(m)):
        row=[]
        for i in range(len(m[0])):
            row.append(m[j][i] - n[j][i])
        result.append(row)
    return result

m=[[53,74,3],
   [46,2,34]]
n=[[3,1,34],
   [24,4,36]]
print("The sum of the matrices is:")
print(addition(m,n))

print("The subtraction of the matrices is:")
print(subtract(m,n))

m=[[9,3,48],
   [8,79,9],
   [8,8,8]]
n=[[5,6],
   [9,8]]
print("The sum of the matrices is:")
print(addition(m,n))
