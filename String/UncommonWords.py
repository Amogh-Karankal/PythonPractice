##Python program to find uncommon words from two Strings

def Uncommon(A, B):
    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1

    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

C = "Amogh Balkrishna Karankal"
D = "Karankal Amogh"
 
# Print required answer
print(Uncommon(A, B))
print(Uncommon(C, D))
