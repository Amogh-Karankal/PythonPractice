##Python Program for Insertion Sort

#iterative
def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


#recursive
def insertion_sort1(arr, n):
    if n <= 1:
        return

    insertion_sort1(arr, n-1)

    last = arr[n-1]
    j = n-2
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = last

A = [-7, 11, 6, 0, -3, 5, 10, 2]
n = len(A)
insertion_sort1(A, n)
print(A)


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
lst = [] #empty list to store sorted elements
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])     #appending the elements in sorted order
print(lst)


