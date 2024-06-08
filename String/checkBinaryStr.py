##Check if a given string is binary string or not

#method 1 - using set
def checkBin(string):
    p = set(string)
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        print("yes")
    else:
        print("No")


#method 2 - simple iteration
def checkBin2(string):
    t = '01'
    count = 0
    for char in string:
        if char not in t:
            count = 1
            break
        else:
            pass

    if count:
        print("No")
    else:
        print("yes")


#method 3 - using regular expression
import re
def checkBin3(string):
    c = re.compile('[^01]')
    if(len(c.findall(string))):
        print("No")
    else:
        print("Yes")


#method 4 - using exception handling
def checkBin4(string):
    try:
        int(string, 2)
    except ValueError:
        return "No"
    return "Yes"


#method 5 - using count()
def checkBin5(string):
    if (string.count('0') + string.count('1') == len(string)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    string1 = "101010000111"
    string2 = "001021010001010"

    checkBin(string1)
    checkBin(string2)

    checkBin2(string1)
    checkBin2(string2)

    checkBin3(string1)
    checkBin3(string2)

    print(checkBin4(string1))
    print(checkBin4(string2))

    checkBin5(string1)
    checkBin5(string2)