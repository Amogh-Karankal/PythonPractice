#Reverse words in a given String

def revStr(s):
    s = s.split()[::-1]
    l = []

    for i in s:
        l.append(i)
    
    return ' '.join(l)

s = "geeks quiz practice code"
print(revStr(s))

#using split function

def revStr1(s):
    words = s.split(' ')
    reverse_s = ' '.join(reversed(words))

    return reverse_s

s = "geeks quiz practice code"
print(revStr1(s))


#using re.findall() function

import re
def revStr2(s):
    words = re.findall('\w+', s)
    rev_s = ' '.join(words[i] for i in range(len(words)-1, -1, -1))

    return rev_s

s = "geeks quiz practice code"
print(revStr2(s))