##Least Frequent Character in String

#naive method
test_str = "GeeksforGeeks"
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i] = 1

res = min(all_freq, key= all_freq.get)

print ("The minimum of all characters in GeeksforGeeks is : " + str(res))

#using collections
from collections import Counter

res1 = Counter(test_str)
res1 = min(res1, key= res1.get)

print ("The minimum of all characters in GeeksforGeeks is : " + str(res))


##Maximum frequency character in String

#naive method
for i in test_str:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i] = 1

res2 = max(all_freq, key= all_freq.get)

print ("The maximum of all characters in GeeksforGeeks is : " + str(res2))

#using collections
from collections import Counter

res3 = Counter(test_str)
res3 = max(res3, key= res3.get)

print ("The maximum of all characters in GeeksforGeeks is : " + str(res3))