##Python | Permutation of a given string using inbuilt function

#method-1: using list
from itertools import permutations

def allPer(str):
    permList = permutations(str)

    for perm in list(permList):
        print(' '.join(perm))

if __name__ == "__main__":
    str = "ABC"
    allPer(str)

##Python | Check for URL in a String

import re

def findURL(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", findURL(string))


