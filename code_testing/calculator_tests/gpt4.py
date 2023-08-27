# after the calculator class creation, I asked GPT4 to create test cases
# and run them in current environment

# Defining the Calculator class first
class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self.result

    def subtract(self, value):
        self.result -= value
        return self.result

    def multiply(self, value):
        self.result *= value
        return self.result

    def divide(self, value):
        if value == 0:
            raise ValueError("Cannot divide by zero!")
        self.result /= value
        return self.result

    def clear(self):
        self.result = 0
        return self.result


# Now, defining the test cases
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5), 5)
        self.assertEqual(self.calculator.add(3), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5), -5)
        self.assertEqual(self.calculator.subtract(3), -8)

    def test_multiply(self):
        self.calculator.add(2)  # set the current value to 2
        self.assertEqual(self.calculator.multiply(3), 6)
        self.assertEqual(self.calculator.multiply(0), 0)

    def test_divide(self):
        self.calculator.add(8)  # set the current value to 8
        self.assertEqual(self.calculator.divide(2), 4)

        # Check division by zero
        with self.assertRaises(ValueError):
            self.calculator.divide(0)

    def test_clear(self):
        self.calculator.add(100)
        self.assertEqual(self.calculator.clear(), 0)


# Executing the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
unittest.TextTestRunner().run(suite)
