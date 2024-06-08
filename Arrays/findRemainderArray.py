#Program for Find remainder of array multiplication divided by n

from functools import reduce
def findRemainder(arr, n):
    multiply = reduce(lambda x, y: x*y, arr)
    answer = multiply % n
    return answer

arr = [2, 5]
n = 3
print(findRemainder(arr, n))

