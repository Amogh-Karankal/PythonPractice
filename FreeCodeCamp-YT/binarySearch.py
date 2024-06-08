def itr_binary(arr, start, end, target):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid-1
        else:
            return mid
            # break

    return -1


def recur_binary(arr, start, end, target):
    if start<=end:
        mid = start+end-1 // 2
        if arr[mid]<target:
            return recur_binary(arr, mid+1, end, target)
        elif arr[mid]>target:
            return recur_binary(arr, start, mid-1, target)
        else:
            return mid
    else:
        return -1

arr = [2,5,10,3,4]
arr.sort()
target = 10
result = itr_binary(arr, 0, len(arr)-1, target)
result1 = recur_binary(arr, 0, len(arr)-1, target)

if result != -1:
    print("at index ", result)
else:
    print("not found")

if result1 != -1:
    print("at index ", result1)
else:
    print("not found")