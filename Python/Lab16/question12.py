X=[[8,5,4],[6,5,3],[7,4,2]]
Y=[[6,5,4],[7,4,2],[8,5,3]]
Z=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(X)):
    for j in range (len(X[0])):
        Z[i][j] = X[i][j] - Y[i][j]
for i in Z:
    print(i)
