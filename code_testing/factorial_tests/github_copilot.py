def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial_list(list):
    return [factorial(x) for x in list]


# create test cases for factorial function

# test the factorial function
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(7) == 5040
assert factorial(8) == 40320
assert factorial(9) == 362880
assert factorial(10) == 3628800

# test the factorial list function
assert factorial_list([1,2,3,4,5,6,7,8,9,10]) == [1,2,6,24,120,720,5040,40320,362880,3628800]
