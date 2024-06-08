#obtain required column from matrix in python

import numpy as np
test_list = np.array([[4, 5, 6], [8, 1, 10], [7, 12, 5]])
print(test_list)
k = int(input("Enter the column number: "))

res = [col[k] for col in test_list]

print(str(res))

#using zip()

test_list1 = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
K = int(input("Enter the column number: "))

# res = list(zip(*test_list)[k])
res = list(zip(*test_list))[K]

print(str(res))
