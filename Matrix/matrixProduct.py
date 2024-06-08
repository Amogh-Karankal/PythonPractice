#Matrix Product - product of all the items in the matrix

def prod(val):
    res = 1
    for ele in val:
        res = res * ele
    
    return res

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

res = prod([ele for sub in test_list for ele in sub])

print(str(res))
