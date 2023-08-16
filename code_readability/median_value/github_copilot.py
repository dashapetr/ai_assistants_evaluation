# find a median value for a given list

def median_value(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)] + list[int(len(list)/2) - 1]) / 2
    else:
        return list[int(len(list)/2)]


print(median_value([1,2,3,4,5,6,7,8,9,10]))
