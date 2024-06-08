#using loops
def palin(s):

    mid = (len(s)-1) // 2
    start = 0
    end = len(s) - 1
    flag = 0

    while(start <= mid):
        if s[start] == s[end]:
            start += 1
            end -= 1

        else:
            flag = 1
            break

    if flag == 0:
        print("a palindrome")
    else:
        print("not a palindrome")


def symm(s):
    n = len(s)
    flag = 0

    if n%2:
        mid = n//2 + 1
    else:
        mid = n//2

    start1 = 0
    start2 = mid

    while(start1 < mid and start2 < n):
        if s[start1] == s[start2]:
            start1 = start1 + 1
            start2 = start2 + 1
        
        else:
            flag = 1
            break

    if flag == 0:
        print("symmetrical")
    else:
        print("not symmetrical")

string = 'amaama'
palin(string)
symm(string)


#using the slicing method

string = 'amaama'
half = int(len(string) / 2)

if len(string)%2 == 0:
    f_string = string[:half]
    s_string = string[half:]
else:
    f_string = string[:half]
    s_string = string[half+1:]

#symmetric or not

if f_string == s_string:
    print("symmetrical")
else:
    ("not symmetrical")

#palindrome or not
if f_string == s_string[::-1]:
    print("a palindrome")
else:
    print("not a palindrome")

