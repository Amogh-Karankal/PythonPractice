#program to add two Matrices

#using for loop

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


#using list comprehension

result1 = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
for r in result1:
    print(r)


#using zip and sum

result2 = [map(sum, zip(*t)) for t in zip(X, Y)]

print(result2)