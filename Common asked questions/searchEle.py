arr = list(map(int, input().split()))
ele = int(input("Enter element to search: "))

flag = 0
for i in arr:
    if i == ele:
        print("ele found")
        flag = 1
        break

if flag == 0:
    print("ele not found")

