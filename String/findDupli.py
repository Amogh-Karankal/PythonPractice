##Python – Find all duplicate characters in string

#method-1: using Counter() method
from collections import Counter

def find_dupli(string):
    wc = Counter(string)
    for letter,count in wc.items():
        if count>1:
            print(letter)


#method-2: using count()
def find_dupli1(string):
    x = []
    for i in string:
        if i not in x and string.count(i)>1:
            x.append(i)
    
    print(" ".join(x))


#method-3: using filter()

def find_dupli2(string):
    x = filter(lambda x: string.count(x)>=2, string)
    print(' '.join(set(x)))



if __name__ == "__main__":
    string = 'geeksforgeeks'
    find_dupli(string)
    find_dupli1(string)
    find_dupli2(string)