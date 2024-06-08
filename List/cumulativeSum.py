#Python program to find Cumulative sum of a list

#using list comprehension and list slicing.

def cumulativeSum(arr):
    cu_list = []
    length = len(arr)
    cu_list = [sum(arr[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]

lists = [10, 20, 30, 40, 50]
print (cumulativeSum(lists))