##Python Program for Linear Search

#Iterative approach
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    
    return -1

#Recursive approach
def linear_search1(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return linear_search1(arr, curr_index-1, key)


arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
curr_index = 4
key = 20

print("x is at index: ", linear_search(arr, x))
print("x is at index: ", linear_search1(arr, curr_index, key))