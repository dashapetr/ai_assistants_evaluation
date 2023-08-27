# for each value in a given list find its factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in lst:
        print(factorial(i))


main()
