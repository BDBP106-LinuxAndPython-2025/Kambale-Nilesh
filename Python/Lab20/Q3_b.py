# (b) Next, in a new program, read in the matrix of strings in the above file as a 2D array
# of list of lists. The number of rows and columns are not known in advance. Make
# sure your code can figure out how many rows and columns are there in this input.
# Name this list as grid and print this 2D list. Name this program as ”Q3 b.py”. In
# this same program, print a list that contains lists of columns of the above matrix.
# For example, the first column will be grouped into a list [A,E,I] and so on. Next,
# print a list that prints the diagonal elements read in one direction. For example,
# some of the elements in this list will be [‘A’],[‘B’,‘E’],[’C’,‘F’,‘I’] and so on.
#from contextlib import nullcontext

basedir='/home/ibab/lab/Kambale-Nilesh/Python/Lab20'
fnew = open(basedir + "/stringmatrix.dat", "r+")
f=fnew.readlines()
grid=[]

for line in f:
     grid.append(line.strip().split())
print(grid)
row = len(grid)
col = len(grid[0])
print(f'number of row in input {row} and column {col} ')
list_col=[]

for i in range(col):
    L2=[]
    for j in range(row):
        L2.append(grid[j][i])
    list_col.append(L2)
print(f'list of column: {list_col}')

diag=[]
for i in range(row + col - 1):
    current_diagonal = []
    for r in range(row):
        c= i-r
        if (0 <= c) & (c < col) :
            current_diagonal.append(grid[r][c])

    diag.append(current_diagonal )
print("Diagonals :")
for d in diag:
    print(d)










