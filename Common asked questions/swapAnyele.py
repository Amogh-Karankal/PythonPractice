arr = list(map(int, input().split()))

pos1 = int(input())
pos2 = int(input())
# arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

# ele1 = arr.pop(pos1)
# ele2 = arr.pop(pos2-1)
# arr.insert(pos1, ele2)
# arr.insert(pos2, ele1)

get = (arr[pos1], arr[pos2])
arr[pos2], arr[pos1] = get

print(arr)