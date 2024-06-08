lst = list(map(int,input().split()))

max = lst[0]
min = lst[0]

l = len(lst)

for i in range(1, l):
    if lst[i] > max:
        max = lst[i]

for i in range(1, l):
    if lst[i] < min:
        min = lst[i]

print(max)
print(min)