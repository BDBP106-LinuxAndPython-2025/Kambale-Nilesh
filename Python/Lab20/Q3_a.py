# (a) Create a simple text file containing the following string matrix, and save it as
# ‘stringmatrix.dat’. This should be saved as a separate program called ”Q3 a.py”.
# (Hint: For those aware of ascii values for alphabets and know how to use them, the
# ascii value of ‘A’ is 65, and one can get the alphabet string by calling chr(65).)
# A B C D
# E F G H
# I J K L

# def genfile(a):
#      for i in a:
#
# L=list(range(65,77))
# print(genfile(L))
def genfile():
    with open("stringmatrix.dat","w") as f:
        matrix = []
        start = 65
        for i in range(3):
            row = []
            for j in range(4):
                row.append(chr(start))
                start = start + 1
            matrix.append(row)
            f.write(" ".join(row) + "\n")
        print(matrix)
        f.close()
        print("file stringmatrix.dat with required data ")

print(genfile())