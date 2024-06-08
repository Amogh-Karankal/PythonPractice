arr = list(map(int, input().split()))
n = len(arr)

# arr[0], arr[n-1] = arr[n-1], arr[0]

# temp = arr[0]
# arr[0] = arr[n-1]
# arr[n-1] = temp

# get = (arr[n-1], arr[0])
# arr[0], arr[n-1] = get

# start, *middle, end = arr
# arr = [end, *middle, start]
first = arr.pop(0)
last = arr.pop(-1)

arr.insert(0, last)
arr.append(first)


print(arr)
