#Matrix creation of n*n

#using list comprehension

dim = int(input("Enter the dimension of the square matrix: "))

res = [list(range(1+dim*i, 1+dim*(i+1))) for i in range(dim)]
print(str(res))

#using next() + itertools.count()

import itertools

dim = int(input("Enter the dimension of the square matrix: "))

temp = itertools.count(1)
res1 = [[next(temp) for i in range(dim)] for i in range(dim)]

print(str(res1))