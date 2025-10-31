#(7)Explore the set_printoptions() function to pretty - print a numpy array by suppressing the scientific notation(like1e10)
import numpy as np

arr = np.array([1.3896e10,2,3,4,1e10], dtype=np.float64)
print(arr)
print(f'before setting suppress {arr}')
np.set_printoptions(suppress=True,formatter={'float_kind': lambda x: f"{x:.3f}"})

print(f'after setting suppress {arr}')
