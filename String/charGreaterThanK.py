##Find words which are greater than given length k

#traverse through all words

def string_x(k, str):
    res = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            res.append(x)
    
    return res

if __name__ == "__main__":
    k = 3
    inputText = "abdh kaj jfhg jdhf jhdfhahs j j j jfa jk j kk kk jj hh ut hf"
    print(string_x(k, inputText))

    #using list comprehension
    sentence = "hello geeks for geeks is computer science portal"
    k1 = 4
    print([word for word in sentence.split() if len(word) > k1])

    #using lanbda function
    k2 = 2
    s = sentence.split(" ")
    l = list(filter(lambda x: (len(x) > k2), s))
    print(l)

