arr = list(map(int, input().split()))

n = int(input())

# count = 0
# for i in arr:
#     if i == n:
#         count+=1

# print(count)

# print(arr.count(n))

from collections import Counter

dic = Counter(arr)

print(dic[n])