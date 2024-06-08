#vertical Concatenation in Matrix

#using loops

test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]

res = []
N = 0

while N != len(test_list):
    temp = ''
    for idx in test_list:
        try: temp = temp + idx[N]
        except IndexError: pass
    
    res.append(temp)
    N = N + 1

res = [ele for ele in res if ele]

print(str(res))

#using join, list comprehension and zip

from itertools import zip_longest

test_list1 = [["Gfg", "good"], ["is", "for"], ["Best"]]

res = ["".join(ele) for ele in zip_longest(*test_list1, fillvalue="")]

print(str(res))