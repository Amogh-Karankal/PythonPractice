def sumOfArr(arr):
    sum = 0
    for i in arr:
        sum += i

    return sum

arr = [12, 3, 4, 5]

ans = sumOfArr(arr)
print("Sum of the array = ", ans)

#using function
ans1 = sum(arr)
print("Sum using inbuilt function = ", ans1)