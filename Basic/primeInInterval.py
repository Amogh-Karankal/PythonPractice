def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list



n1 = int(input("Enter the starting integer: "))
n2 = int(input("Enter the ending integer: "))
prime_list = prime(n1, n2)
if len(prime_list) == 0:
    print("No prime numbers available!!")
else:
    print("Prime numbers between these integers: ", prime_list)