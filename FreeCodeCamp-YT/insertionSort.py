def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key
    
    return arr

arr = [12,4,54,6,7,8,66,88,9]
print(insertion_sort(arr))