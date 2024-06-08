#Program for Sum of squares of first n natural numbers


#in O(N) time

def sqsum(n):
    ans = 0
    for i in range(1, n+1):
        ans = ans + (i*i)

    return ans

num = int(input("Enter a natural number: "))
print("Sum of squares of first ", num, " numbers = ", sqsum(num))


#in O(1)
# given formmula: (N * (N + 1) * (2 * N + 1)) / 6

def sqsum1(n):
    return (n * (n + 1) * (2*n + 1)) // 6

num = int(input("Enter a natural number: "))
print("Sum of squares of first ", num, " numbers = ", sqsum1(num))