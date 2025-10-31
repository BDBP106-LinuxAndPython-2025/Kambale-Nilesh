#(1) Import numpy and check the version using the command print(np.__version__)
import numpy as np
import sys
print(np.__version__)
print("(2) Array creation and manipulation exercises. Print all the arrays in each exercise.")

print('(i) Create a 1D array from 0 to 9')
a = np.arange(10)
print(a)

print("(ii) Create a boolean array of size 3x3.")
#b = np.array([[[[0,1,0],[0,1,0],[1,0,0]],[[1,0,1],[1,0,1],[1,0,1]],[[1,0,1],[0,0,0],[1,1,1]]],[[[0,1,0],[0,1,0],[1,0,0]],[[1,0,1],[1,0,1],[1,0,1]],[[1,0,1],[0,0,0],[1,1,1]]],[[[0,1,0],[0,1,0],[1,0,0]],[[1,0,1],[1,0,1],[1,0,1]],[[1,0,1],[0,0,0],[1,1,1]]]], dtype=bool)
#print(b)
#c = np.random.choice(a=[True, False], size=(3,3,3)) # another way
#print(c)
d = np.full((3,3,3,3), [True, True, False])
print(d)

print('(iii) Using syntax from list comprehension, create an array that satisfies the condition.'
      'For example,arr = np.arange(10) '
      'arr = arr[ arr%2 == 1 ]')
#Create an array of prime numbers from 1 to 50 using a similar approach

arr = np.array([n for n in range(2, 51) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))])
print(arr)

print("iv) Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print the two arrays.")
e = np.arange(20)
print(e)
f = e.reshape(4,5)
print(f)
#print(np.arange(20).reshape(4,5)

print("(v) Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has only 1s. Then stack the two arrays horizontally.")
g = np.arange(10)
h = np.ones(10)
i = np.column_stack((g,h))
print(i)

print(" (vi) Define two 1D arrays, where array a has list of first 100 numbers, and b has first "
      "100 prime numbers. Obtain a new array that is the intersection "
      "of these two arrays (Hint: use np.intersect1d())")
j = np.arange(100)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
k = np.array([ n for n in range(2,1000) if is_prime(n) ])[:100]
l = np.intersect1d(j, k)
print(l)

print("vii) Use the above two arrays with the aim this time to remove items from a that arein "
      "b. (We are doing a-b operation, use np.setdiff1d())")
m = np.setdiff1d(j, k)
print(m)

print("(viii) Use the above two arrays with the aim of getting the indices of common elements,between the two arrays. (Hint: Use np.where(a==b))")
k = np.array([ n for n in range(2,1000) if is_prime(n) ])[:100]
j = np.arange(100)
n = np.where( j == k )
print(n)
print("(ix) Extract the elements of the array a above that are greater than 5 and less than 20.")
o = j[(j > 5) & (j < 21)]
print(o)








