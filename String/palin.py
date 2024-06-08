def isPalin(s):
    return s == s[::-1]

s1 = "malayalam"
ans1 = isPalin(s1)
s2 = "Amogh"
ans2 = isPalin(s2)
 
if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")


#iterative method

def isPalin1(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    
    return True

s1 = "malayalam"
ans1 = isPalin1(s1)
s2 = "Amogh"
ans2 = isPalin1(s2)
 
if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")


#inbuilt fucntion

def isPalin2(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True

    return False

s1 = "malayalam"
ans1 = isPalin2(s1)
s2 = "Amogh"
ans2 = isPalin2(s2)
 
if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")


#using extra variable
def isPalin3(s):
    rev = ''
    for i in s:
        rev = i + rev
    if (s == rev):
        return True

    return False

s1 = "malayalam"
ans1 = isPalin3(s1)
s2 = "Amogh"
ans2 = isPalin3(s2)
 
if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")


#using flag
def isPalin4(s):
    j = -1
    flag = 0
    for i in s:
        if i != s[j]:
            flag = 1
            break
        j = j - 1
    if flag == 1:
        return False
    else:
        return True

s1 = "malayalam"
ans1 = isPalin4(s1)
s2 = "Amogh"
ans2 = isPalin4(s2)
 
if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")


#using recursion
def isPalin5(s):
    s = s.lower()
    l = len(s)

    if l < 2:
        return True
    
    elif s[0] == s[l - 1]:
        return isPalin5(s[1: l - 1])

    else:
        return False

s1 = "malayalam"
ans1 = isPalin5(s1)
s2 = "Amogh"
ans2 = isPalin5(s2)
 
if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")