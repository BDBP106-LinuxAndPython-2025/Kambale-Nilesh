#(4) Thinking along the same lines of the above question, how will you swap two columns in
#a 2D array? Define a 3x3 matrix with random values, and swap first and second columns
#in this array.
import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [10,11,12,13],
                  [14,15,16,17]
                  ])

array[:, [0, 1]] = array[:,[1, 0]]
print(array)




