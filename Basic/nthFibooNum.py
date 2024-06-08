def fibo(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input("Enter an integer: "))

print(fibo(n), " is the ", n, " number in the Fibonacci Series")

# using dynamic programming

fib_array = [0, 1]


def fibo1(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(fib_array):
        return fib_array[n - 1]
    else:
        temp_fib = fibo1(n - 1) + fibo1(n - 2)
        fib_array.append(temp_fib)
        return temp_fib


n = int(input("Enter an integer: "))

print(fibo1(n), " is the ", n, " number in the Fibonacci Series")


# using dynamic programming with space optimization

def fibo2(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


n = int(input("Enter an integer: "))

print(fibo2(n), " is the ", n, " number in the Fibonacci Series")


# using arrays

def fibo3(n):
    if n <= 0:
        print("Incorrect input")
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i - 1] + data[i - 2])
    return data[n - 1]


n = int(input("Enter an integer: "))

print(fibo3(n), " is the ", n, " number in the Fibonacci Series")

# using direct formula

from math import sqrt


def fibo4(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            answer = (((1 + sqrt(5)) ** n) - ((1 - sqrt(5))) ** n) / (2 ** n * sqrt(5))

        return answer


n = int(input("Enter an integer: "))

print(int(fibo4(n)), " is the ", n, " number in the Fibonacci Series")
