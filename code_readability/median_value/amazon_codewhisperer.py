# find a median value for a given list


def median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2] + sorted_lst[length // 2 - 1]) / 2
    else:
        return sorted_lst[length // 2]


print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# output: 5.5

print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

# output: 6.0
