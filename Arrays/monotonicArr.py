# Program to check if given array is Monotonic

# An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing
# if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

def isMonotonic(arr):
    return(all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)) or
           all(arr[i] >= arr[i+1] for i in range(len(arr) - 1)))


arr1 = [6, 5, 4, 4]
arr2 = [5, 12, 34, 56]

arr3 = [34, 32, 54, 67, 77]
arr4 = [4]
print(isMonotonic(arr1))
print(isMonotonic(arr2))
print(isMonotonic(arr3))
print(isMonotonic(arr4))
