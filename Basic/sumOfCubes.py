#program to calculate the sum of cubes of first n natural numbers

def cubesum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i*i*i)

    return sum

num = int(input("Enter a natural number: "))
print("Sum of cubes of first ", num, " numbers = ", cubesum(num))


#using formula
# ((N * (N + 1))/2) ^ 2

def cubesum1(n):
    x = (n * (n + 1)) // 2
    return (int) (x * x)

num = int(input("Enter a natural number: "))
print("Sum of cubes of first ", num, " numbers = ", cubesum1(num))