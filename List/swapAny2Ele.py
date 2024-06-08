#program to swap two elements in a list
#different fuctions with different approaches

def swapElement(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

arr = [1, 2, 3, 5, 4, 6]
pos1 = 3
pos2 = 4
print(swapElement(arr, pos1, pos2))

def swapElement1(list, pos1, pos2):
    a = list.pop(pos1)
    b = list.pop(pos2 - 1)

    list.insert(pos1, b)
    list.insert(pos2, a)

    return list

arr = [1, 2, 3, 5, 4, 6]
pos1 = 3
pos2 = 4
print(swapElement1(arr, pos1, pos2))


def swapElement2(arr, pos1, pos2):
    temp = arr[pos1], arr[pos2]
    arr[pos2], arr[pos1] = temp

    return arr

arr = [1, 2, 3, 5, 4, 6]
pos1 = 3
pos2 = 4
print(swapElement2(arr, pos1, pos2))