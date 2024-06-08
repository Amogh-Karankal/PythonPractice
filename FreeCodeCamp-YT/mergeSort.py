def sortArr_recursive(A):
    if len(A)<=1:
        return A
    middle = len(A)//2
    left = sortArr_recursive(A[:middle])
    right = sortArr_recursive(A[middle:])
    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged.extend(right if right else left)
    return merged

def sortArr_itr(arr):
    mid = len(arr)//2
    left = sorted(arr[:mid])
    right = sorted(arr[mid:])
    c = []

    while min(len(left), len(right))>0:
        if left[0]>right[0]:
            insert = right.pop(0)
            c.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            c.append(insert)
    
    if len(left)>0:
        for i in left:
            c.append(i)
    if len(right)>0:
        for i in right:
            c.append(i)

    return c


arr = [2,3,5,4,6,5,7,5]
print(sortArr_recursive(arr))
print(sortArr_itr(arr))



