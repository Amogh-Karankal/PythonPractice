##String slicing in Python to rotate a string

#method-1: string slicing approach

def rotate(string, d):
    lFirst = string[0 : d]
    lSecond = string[d :]
    rFirst = string[0 : len(string) - d]
    rSecond = string[len(string) - d :]

    print("Left Rotation: ", (lSecond + lFirst))
    print("Right rotation: ", (rSecond + rFirst))



#method-2: using extended string

def rotate1(string, d):
    temp = string + string
    l1 = len(string)
    l2 = len(temp)
    lFirst = temp[d : l1+d]
    lSecond = temp[l1-d : l2-d]

    print("Left rotation: ", lFirst)
    print("Right rotation: ", lSecond)

if __name__ == "__main__":
    string = input("Enter a string: ")
    d = int(input("Enter how many letters to rotate: "))
    rotate(string, d)
    rotate1(string, d)


