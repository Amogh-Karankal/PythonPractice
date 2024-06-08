def NmaxElements(arr, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(arr)):
            if arr[j] > max1:
                max1 = arr[j]

        arr.remove(max1)
        final_list.append(max1)

    print(final_list)

arr = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

NmaxElements(arr, N)

l = [1000,298,3579,100,200,-45,900]
l.sort()
print(l[-N:])
