#Python | Count the Number of matching characters in a pair of string

#using counter variable
def count(str1, str2):
    c, j = 0, 0

    for i in str1:
        if str2.find(i)>=0 and j == str1.find(i):
            c+=1
        j+=1

    print("No. of matching characters are: ", c)


#using set() to remove duplicates

def count1(str1, str2):
    str_1 = set(str1)
    str_2 = set(str2)

    # using (&) intersection mathematical operation on sets
    # the unique characters present in both the strings
    # are stored in matched_characters set variable
    match_str = str_1 & str_2

    print("No. of matching characters are: ", str(len(match_str)))


#using regular expression
import re

def count2(str1, str2):
    c = 0
    for i in str1:
        if re.search(i, str2):
            c += 1

    print("No. of matching characters are: ", c)



def main():
    str1 ='aabcddekll12_' # first string
    str2 ='bb2211@55k' # second string
    count(str1, str2)
    count1(str1, str2)
    count2(str1, str2)

if __name__ == "__main__":
    main()
