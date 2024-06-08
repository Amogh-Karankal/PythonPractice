n1 = 0
n2 = 1
num = int(input())
print(n1)
print(n2)

for i in range(2, num):
    sum = n1+n2
    print(sum)
    n1 = n2
    n2 = sum

