#Remove all duplicates from a given string in Python

#method 1 - using OrderDict

from collections import OrderedDict

def removeWithoutOrder(str):
    return "".join(set(str))

def removeWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

    
#method 2 - using normal for loop

def removeDupli(str):
    s = set(str)
    s = "".join(s)
    print("Without order: ", s)

    t = ""
    for i in str:
        if i in t:
            pass
        else:
            t = t + i
        print("With order: ", t)

if __name__ == "__main__":
    str = "geeksforgeeks"
    print("Without order: ", removeWithoutOrder(str))
    print("With order: ", removeWithOrder(str))
    str = "geeksforgeeks"
    removeDupli(str)


