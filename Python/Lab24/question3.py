#(3) We know how to reverse the elements in a 1D array- a[::-1]. How would you reverse
#the rows in a 2D array? How would you reverse the columns in a 2D array?
import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [10,11,12,13],
                  [14,15,16,17]
                  ])

print(array[::-1]) # [] reresent sub script  It will give rows in reverse
print(array[:,::-1])  #  in firs :, before is for rows & Default & ::-1 if for colum to verse column