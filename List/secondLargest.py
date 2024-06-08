#program to find second largest number in a list


def secondLargest(arr):

    arr1 = list(set(arr)) #to remove duplicate values
    mx = max(arr1[0], arr1[1])
    smx = min(arr1[0], arr1[1])

    n = len(arr1)

    for i in range(2, n):
        if arr1[i]>mx:
            smx = mx
            mx = arr1[i]
        elif arr1[i]>smx:
            mx != arr1[i]
            smx = arr1[i]

    return smx

list1 = [10, 20, 4, 45, 99, 45, 20, 34, 45, 33, 22, 10]
list2 = list(set(list1))
list2.sort()
print(list2)
print(secondLargest(list1))



def secondLargest1(arr): #using list comprehension
    sublist = [x for x in arr if x < max(arr)]
    return max(sublist)

list1 = [10, 20, 4, 45, 99, 45, 20, 34, 45, 33, 22, 10]
list2 = list(set(list1))
list2.sort()
print(list2)
print(secondLargest1(list1))