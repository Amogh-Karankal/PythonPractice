import math


def checkPerfectSq(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibo(n):
    return checkPerfectSq(5 * n * n + 4) or checkPerfectSq(5 * n * n - 4)


n = int(input("Enter an integer: "))

if isFibo(n):
    print(n, " is a Fibonacci number")
else:
    print(n, " is not a Fibonacci number")
