# create a calculator class

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
