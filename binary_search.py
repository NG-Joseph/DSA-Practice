test_list = [10, 20, 21, 22, 24, 27] # must be sorted for binary search to work


def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        # // is floor division. Rounds down to the nearest whole number
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


print(binary_search(test_list, 22))


