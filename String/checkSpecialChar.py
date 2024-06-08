##Program to check if a string contains any special character

#using regular expression

import re

def findSpecial(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(regex.search(string) == None):
        print("No special characters. String is accepted!")
    else:
        print("Contains special characters. String is not accepted!")

#using for loop
def findSpecial1(str):
    str.split()
    c = 0
    s = '[@_!#$%^&*()<>?/\|}{~:]' 
    for i in range(len(str)):
        if str[i] in s:
            c += 1
    
    if c:
        print("Contains special characters. String is not accepted!")
    else:
        print("No special characters. String is accepted!")
    


if __name__ == "__main__":
    str = "Geeks$For$Geeks"

    findSpecial(str)
    findSpecial(str)