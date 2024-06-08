##Python – Replace all occurrences of a substring in a string

#method-1: inbuilt function replace present in python3 to replace all occurrences of substring.

def replaceStr(string, s1, s2):
    string = string.replace(s1, s2)
    print(string)


#method-2: Splitting the string by substring and then replacing with the new string.split() function is used.

def replaceStr1(string, s1, s2):
    s = string.split(s1)
    new_str = ""

    for i in s:
        if (i == ""):
            new_str += s2
        else:
            new_str += i
    
    print(new_str)


if __name__ == "__main__":
    string = input("Enter any string: ")
    s1 = input("Enter substring to be replaced: ")
    s2 = input("Enter the string to replace the substring: ")
    replaceStr(string, s1, s2)
    replaceStr1(string, s1, s2)