def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr=[1,2,3,4,5,6,7,8,9]
target = 4
print(linear_search(arr, target))