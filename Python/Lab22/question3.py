# (3) Implement matrix multiplication of matrices A and B without using any external pack-
# ages as an instance method in a class called LinearAlgebra. Get the no. of rows and
# columns and elements of each matrix from the user. Raise errors in case the condition
# for matrix multiplication is not met. Once you have a working code for this, decorate a
# function that returns the matrices A and B using @property. Then also define a setter
# function to allow the modification of A and B, since the user may make mistakes in
# inputting the matrices and should be able to change elements as desired. Lastly, define
# a custom decorator for calculating time in multlplying matrices A and B of size 50x50.
A=[[1,2,3],[4,5,6]]
B=[[6,4],[7,8],[9,10]]
import time
def timme_taken(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken: {end - start:.6f}')
        return result
    return wrapper

class MatriMultiplication:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if len(a[0]) != len(b):
            raise ValueError('The number of elemnt of first matrix must be same as number of rows of second matrix ')

    @property
    def A(self):
        return self.a

    @A.setter
    def A(self,mod_a):
        self.a=mod_a

    @property
    def B(self):
        return self.b

    @B.setter
    def B(self,mod_b):
        self.b=mod_b


    @timme_taken
    def linearalgebra(self):
        rows_A=len(self.a)
        cols_A=len(self.a[0])
        rows_B=len(self.b)
        cols_B=len(self.b[0])

        if cols_A!=rows_B:
            raise ValueError('The number of elements of first matrix must be same as number of rows of second matrix ')

        AB=[[0 for i in range(cols_B)] for j in range(rows_A) ]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    AB[i][j] += self.a[i][k] * self.b[k][j]

        return AB



# mat1 = [[1, 2, 3], [4, 5, 6]]
# mat2 = [[6, 4], [7, 8], [9, 10]]
#
# result = MatriMultiplication(mat1, mat2)
# print("Matrix Multiplication Result:")
# print(result.linearalgebra())


import random
mat1=[[random.randint(1,4) for _ in range(50)] for _ in range(50)]
mat2=[[random.randint(3,6) for _ in range(50)] for _ in range(50)]

print("------------- Resultant multiplication matrix ------------------ ")
R = MatriMultiplication(mat1,mat2)
for row in R.linearalgebra():
    print(row)






