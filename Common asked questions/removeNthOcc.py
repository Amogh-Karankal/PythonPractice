arr = ["amogh", "karankal", "lol", "amogh", "amogh"]
word = input()
n = int(input())
count = 0

for i in range(0, len(arr)-1):
    if arr[i] == word:
        count+=1
        if count == n:
            del arr[i]

print(arr)

