import math


def factorial1(n):
    return math.factorial(n)


x = int(input("Enter an integer: "))
# ans = factorial(x)
print("factorial of ",x," is ", factorial1(x))


def factorial2(n):
    return 1 if (n==0 or n==1) else n * factorial2(n-1)


x = int(input("Enter an integer: "))
# ans = factorial(x)
print("factorial of ",x," is ", factorial2(x))


def factorial3(n):
    if n < 0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while n>1:
            fact = fact * n
            n -= 1

        return fact


x = int(input("Enter an integer: "))
# ans = factorial(x)
print("factorial of ",x," is ", factorial3(x))