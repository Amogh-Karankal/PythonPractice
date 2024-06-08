#Ways to remove i’th character from string

#naive method
def removeChar(s,i):
    new_str = ""
    for j in range(len(s)):
        if j != i:
            new_str = new_str + s[j]

    return new_str

test_str = "GeeksForGeeks"
print(removeChar(test_str,2))


#using str.replace()

# def removeChar1():
