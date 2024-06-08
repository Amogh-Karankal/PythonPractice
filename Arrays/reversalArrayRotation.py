#Program for Reversal algorithm for array rotation

def reverseArr(arr, s, e):
    while s < e:
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        s += 1
        e = e - 1

def rotateLeft(arr, d):
    n = len(arr)
    reverseArr(arr, 0, d-1)
    reverseArr(arr, d, n-1)
    reverseArr(arr, 0, n-1)

def printArr(arr):
    for i in range(0, len(arr)):
        print(arr[i])

arr = [1, 2, 3, 4, 5, 6, 7]
rotateLeft(arr, 2)
printArr(arr)


