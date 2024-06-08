def sumOfElements(arr):
    ans = 0
    for i in range(len(arr)+1):
        ans = ans + i

    return ans

arr = [1, 2, 3, 4, 5]
print(sumOfElements(arr))