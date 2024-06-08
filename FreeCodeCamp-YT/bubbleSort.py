def bubble_opt(arr):
    itr = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            itr += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr, itr

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_unopt(A):
    itr = 0
    for i in A:
        for j in range(len(A)-1):
            itr+=1
            if A[j]>A[j+1]:
                swap(A,j,j+1)
    return A, itr

arr = [9,8,5,6,4,5,2,3,1]
print(bubble_opt(arr))
print(bubble_unopt(arr))

