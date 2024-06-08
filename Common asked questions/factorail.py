def fact1(n):
    factorial = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            factorial = factorial * i
        return factorial

print(fact1(6))

def fact2(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * fact2(n-1)

print(fact2(6))