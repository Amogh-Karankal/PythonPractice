##Replace duplicate Occurrence in String

#method 1 - using split() + enumerate() + loop

test_str = 'Gfg is best . Gfg also has Classes now. \
                Classes help understand better . '
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing replace mapping
repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }
 
# Replace duplicate Occurrence in String
# Using split() + enumerate() + loop
test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)
 
# printing result
print("The string after replacing : " + str(res))


#method 2 - using keys() + index() + list comprehension

test_str1 = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '

print("The original string is : " + str(test_str1))
 
# initializing replace mapping
repl_dict1 = {'Gfg' : 'It', 'Classes' : 'They' }
test_list1 =  test_str1.split(' ')
res1 = ' '.join([repl_dict1.get(val) if val in repl_dict1.keys() and test_list1.index(val) != idx else val for idx, val in enumerate(test_list1) ])

print("The string after replacing : " + str(res1))
