X = [[1,2],
     [2,3]]
Y = [[2,3],
     [3,4]]

result = [[0,0],
          [0,0]]

for i in range(len(X)): #iterate through rows of X
    for j in range(len(Y)): #iterate through col of Y
        for k in range(len(Y)): #iterate through rows of Y
            result[i][j] += X[i][k] * Y[k][j]

for end in result:
    print(end)