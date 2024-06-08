# method to print the ASCII value of the characters in a string using python:

s = input("Enter a stirng: ")

txtlen = len(s)
for char in s:
    asciiVal = ord(char)
    print(char, "\t", asciiVal)

