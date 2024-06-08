#program to multiply two matrices

#using simple nested loops

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)

#using zip

result1 =[[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]

for r in result1:
    print(r)

#using numpy dot
import numpy as np

result2= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

result2 = np.dot(A, B)

for r in result2:
    print(r)
