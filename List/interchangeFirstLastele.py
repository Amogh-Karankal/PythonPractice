#program to interchange first and last elements in a list
#total 5 fucntions with different approaches

def swapList(arr):
    size = len(arr)

    temp = arr[0]
    arr[0] = arr[size - 1]
    arr[size - 1] = temp
    return arr

arr1 = [1, 2, 4, 3, 5]
print(swapList(arr1))


def swapList1(arr):
    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]

    return arr
arr1 = [1, 2, 4, 3, 5]
print(swapList1(arr1))


def swapList2(arr):
    temp = arr[0], arr[len(arr) - 1]

    arr[len(arr) - 1], arr[0] = temp

    return arr

arr1 = [1, 2, 4, 3, 5]
print(swapList2(arr1))


def swapList3(arr):
    s, *m, e = arr
    arr = [e, *m, s]
    return arr

arr1 = [1, 2, 4, 3, 5]
print(swapList3(arr1))


def swapList4(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list

arr1 = [1, 2, 4, 3, 5]
print(swapList4(arr1))









