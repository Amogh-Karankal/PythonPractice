##Python Program for Binary Search (Recursive and Iterative)

#Recursive
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        else:
            return binary_search(arr, mid+1, high, x)

    else:
        return -1


#Iterative
def binary_search1(arr, x):
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] > x:
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

        else: 
            return mid

    return -1


arr = [2,5,10,3,4]
x = 3
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
result1 = binary_search1(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

if result1 != -1:
    print("Element is present at index", str(result1))
else:
    print("Element is not present in array")