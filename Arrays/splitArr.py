#Program to Split the array and add the first part to the end


def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]
        arr[n-1] = x

arr = [12, 10, 5, 6, 52, 36]

n = len(arr)
k = 2

splitArr(arr, n, k)

for i in range(n):
    print(arr[i], end=" ")


def splitArr1(arr, n, k):
    b = arr[:k]
    return (arr[k::] + b[::])


# arr = [12, 10, 5, 6, 52, 36]
#
# n = len(arr)
# k = 2

splitArr1(arr, n, k)

for i in range(n):
    print('\n', arr[i], end=" ")

