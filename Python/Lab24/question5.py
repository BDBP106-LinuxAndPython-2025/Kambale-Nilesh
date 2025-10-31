#You are given two 1D arrays. Write a function to create a new array that contains the
#maximum of the respective elements in the two arrays. For example, if a=[1,2] and
#b=[0,5] then the new array will be c=[1,5].
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

def maximize_array(x,y):
    if len(x) != len(y):
        raise ValueError("Array must have same length")
    c = np.array([])
    for i in range(len(x)):    #c = [max(a[i], b[i]) for i in range(len(a))]
        if x[i] > y[i]:
            c = np.append(c,x[i])
        else:
            c = np.append(c,y[i])
    return c
print(maximize_array(arr1,arr2))




