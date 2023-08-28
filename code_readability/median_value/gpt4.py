# find a median value for a given list

def find_median(lst):
    """Find the median value of a given list."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    # If the length of the list is even
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    # If the length of the list is odd
    else:
        return sorted_lst[n // 2]


# Test the function with a sample list
sample_list_1 = [5, 2, 9, 1, 5, 6]
sample_list_2 = [7, 2, 9, 3]
median_1 = find_median(sample_list_1)
median_2 = find_median(sample_list_2)
median_1, median_2
