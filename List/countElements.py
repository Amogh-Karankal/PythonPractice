def countElements(arr, x):
    count = 0
    for ele in arr:
        if (ele == x):
            count = count + 1
    
    return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countElements(lst, x))

#using count() function

def countX(arr, x):
    return arr.count(x)

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

#using Counter() from collections library

from collections import Counter

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
ans = Counter(lst)

print(ans[x])
