class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        self.result /= num

    def reset(self):
        self.result = 0

    def get_result(self):
        return self.result

# create tests for calculator class

# create a calculator object
calculator = Calculator()

# test the add method
calculator.add(5)
assert calculator.get_result() == 5

# test the subtract method
calculator.subtract(2)
assert calculator.get_result() == 3

# test the multiply method
calculator.multiply(3)
assert calculator.get_result() == 9

# test the divide method
calculator.divide(3)
assert calculator.get_result() == 3

# test the reset method
calculator.reset()
assert calculator.get_result() == 0
