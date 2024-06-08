#Sum of number digits in List

#using loop + str() - brute force method

def sumOfDigits(arr):
    res = []
    for ele in arr:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)
    return res

test_list = [12, 67, 98, 34]
print(sumOfDigits(test_list))


#using sum() + list comprehension

test_list = [12, 67, 98, 34]

res = list(map(lambda x: sum(map(int, str(x))), test_list))

print(str(res))


#using sum() + reduce()

from functools import reduce

test_list = [12, 67, 98, 34]

res = [reduce(lambda x, y: x + y, map(int, str(ele))) for ele in test_list]

print(str(res))