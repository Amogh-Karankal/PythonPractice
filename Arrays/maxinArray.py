#using linear search

def maxInArray(arr, n):
    maxNum = arr[0]

    for i in range(1, n):
        if arr[i] > maxNum:
            maxNum = arr[i]
    return maxNum

arr = [1, 2, 45, 56, 76, 567, 8898, 578, 43, 2, 6]

n = len(arr)

ans = maxInArray(arr, n)
print("Largest number in the array = ", ans)

#using inbuilt function

ans = max(arr)
print("Largest number using inbuilt function = ", ans)