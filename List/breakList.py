#Break a list into chunks of size N

#using yield

def divideChunks(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i+n]

my_list = ['geeks', 'for', 'geeks', 'like', 'geeky','nerdy', 'geek', 'love', 'questions','words', 'life']
n = 2
x = list(divideChunks(my_list, n))
print(x)

#using list comprehension

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3

final = [my_list[i*n : (i+1)*n] for i in range((len(my_list)+ n - 1)//n)]
print(final)

#alternate implementation

final1 = [my_list[i:i+n] for i in range(0, len(my_list), n)]
print(final1)