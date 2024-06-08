def itr_fact(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    
    return fact
print(itr_fact(5))

def recr_fact(m):
    if m == 1 or m == 0:
        return 1
    else:
        temp = recr_fact(m-1)
        return temp * m

print(recr_fact(5))

def recr_fact1(x):
    if x == 1 or x == 0: return 1
    else: return x * recr_fact1(x-1)

print(recr_fact1(6))
