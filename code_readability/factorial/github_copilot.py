# for each value in a given list find its factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial_list(list):
    return [factorial(x) for x in list]


print(factorial_list([1,2,3,4,5,6,7,8,9,10]))
