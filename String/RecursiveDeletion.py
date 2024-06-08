##Check if a string can become empty by recursively deleting a given sub-string

#method-1: using inbuilt string functions find() and erase().

def canBecomeEmpty(string, sub_str):
    while len(string) > 0:
        idx = string.find(sub_str)
        if idx == -1:
            break

        string = string.replace(sub_str, "", 1)
    
    return (len(string) == 0)


#method-2: using regular expression

import re

def canBecomeEmpty1(string, sub_str):
    while sub_str in string:
        string = re.sub(sub_str, "", string)

    return True if string == "" else False


#method-3: using string slicing

def canBecomeEmpty2(string, pattern):
    if len(string) == 0 and len(pattern) == 0:
        return True
    
    if len(pattern) == 0:
        return True

    while len(string) != 0:
        index = string.find(pattern)

        if index == -1:
            return False
        
        string = string[0:index] + string[index + len(pattern) :]
    
    return True


if __name__ == "__main__":
    string = "GEEGEEKSKS"
    sub_str = "GEEKS"
    if canBecomeEmpty(string, sub_str):
        print("Yes")
    else:
        print("No")

    if canBecomeEmpty1(string, sub_str):
        print("Yes")
    else:
        print("No")

    if canBecomeEmpty2(string, sub_str):
        print("Yes")
    else:
        print("No")