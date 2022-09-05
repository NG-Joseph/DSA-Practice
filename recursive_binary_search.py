test_list = [10, 20, 21, 22, 24, 27] # must be sorted for binary search to work

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint+1], target)



print(recursive_binary_search(test_list, 22))
