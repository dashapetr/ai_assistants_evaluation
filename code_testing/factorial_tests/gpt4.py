# after the factorial function creation, I asked GPT4 to create test cases
# and run them in current environment

# Adjusting the factorial function to handle negative values with a ValueError
def factorial(n):
    """Compute the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative values.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def list_factorials(lst):
    """Compute the factorial for each value in the list."""
    return [factorial(item) for item in lst]

# Writing test cases for the factorial function
class TestFactorial(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(factorial(0), 1)

    def test_small_values(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def test_large_value(self):
        self.assertEqual(factorial(10), 3628800)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_list_factorials(self):
        self.assertEqual(list_factorials([0, 1, 2, 3, 4]), [1, 1, 2, 6, 24])


# Executing the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorial)
unittest.TextTestRunner().run(suite)
