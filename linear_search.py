def linear_search(list, target):
    for item in list:
        if item == target:
            return list.index(item)


# O(n)
def linear_search2(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None



print(linear_search([2,0,3,2,44,3,4,5], 3))