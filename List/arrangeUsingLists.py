#Sort the values of first list using second list 

#using zip()

def sort_list(arr1, arr2):
    zipped_list = zip(arr2, arr1)
    
    z = [x for _, x in sorted(zipped_list)]

    return z

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

print(sort_list(x, y))

#By using Dictionary, list comprehension, lambda function

def sortingList(arr1, arr2):
    f_1 = {}
    final_list = []

    f_1 = {arr1[i]: arr2[i] for i in range(len(arr2))}

    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

    for i in f_lst.keys():
        final_list.append(i)
    
    return final_list

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

print(sortingList(x, y))