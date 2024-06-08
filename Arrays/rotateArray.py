# function to rotate by d elements

# using temp arr

def rotateArr(arr, n, d):
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i += 1
    i = 0
    while d < n:
        arr[i] = arr[d]
        i += 1
        d += 1
    arr[:] = arr[: i] + temp
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation = ", end=' ')
print(rotateArr(arr, len(arr), 2))


# rotating one-by-one

def rotateLeftByOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


# rotate left by d
def rotateLeft(arr, n, d):
    for i in range(d):
        rotateLeftByOne(arr, n)


def printArr(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=' ')

arr = [1, 2, 3, 4, 5, 6, 7]
rotateLeft(arr, len(arr), 2)
printArr(arr, len(arr))
