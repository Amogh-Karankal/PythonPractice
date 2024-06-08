#Program to accept the strings which contains all vowels

def checkString(s):
    input_str = s.lower()

    vowels = set("aeiou")

    ans = set({})

    for char in input_str:
        if char in vowels:
            ans.add(char)
        else:
            pass

    if len(ans) == len(vowels):
        print("Accepted")
    else:
        print("Not accepted")


if __name__ == "__main__":
    string1 = "SEEquoiaL"
    string2 = "amogH kArankal"
    checkString(string1)
    checkString(string2)

