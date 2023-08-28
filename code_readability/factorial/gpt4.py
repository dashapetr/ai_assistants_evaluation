# for each value in a given list find its factorial

def factorial(n):
    """Compute the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def list_factorials(lst):
    """Compute the factorial for each value in the list."""
    return [factorial(item) for item in lst]

# Test the function with a sample list
sample_list = [0, 1, 2, 3, 4, 5]
factorial_results = list_factorials(sample_list)
factorial_results
