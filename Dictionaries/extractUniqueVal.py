##Python – Extract Unique values dictionary values

#method-1: Using sorted() + set comprehension + values()

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

print("The original dictionary is : " + str(test_dict))

res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values list is : " + str(res))


#method-2: Using chain() + sorted() + values()
from itertools import chain
res1 = list(sorted(set(chain(*test_dict.values()))))
print("The unique values list is : " + str(res1))

#method-3: Using keys(),extend(),list(),set() and sort() methods

x = []
for i in test_dict.keys():
    x.extend(test_dict[i])
x = list(set(x))
x.sort()

print("The unique values list is : " + str(x))