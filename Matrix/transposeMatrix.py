#Transpose a matrix in Single line in Python

#using nested list comprehension
m = [[1,2],[3,4],[5,6]]

for row in m:
    print(row)

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print('\n')

for r in rez:
    print(r)
print('\n')

#using zip
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for row in matrix:
    print(row)

print('\n')

t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)
print('\n')

#using numpy

import numpy as np
matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)
print('\n')

print(np.transpose(matrix))
print('\n')

print(matrix.T)