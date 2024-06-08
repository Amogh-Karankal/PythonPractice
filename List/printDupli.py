#Program to print duplicates from a list of integers

def repeatList(arr):
    _size = len(arr)

    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if arr[i] == arr[j] and arr[i] not in repeated:
                repeated.append(arr[i])
    
    return repeated

list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(repeatList(list1))