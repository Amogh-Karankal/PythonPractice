arr = list(map(int, input().split()))

prod = 1

for i in arr:
    prod = prod * i
print(prod)

import numpy
print(numpy.prod(arr))
