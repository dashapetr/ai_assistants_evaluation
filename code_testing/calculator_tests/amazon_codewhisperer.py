class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def mod(self):
        return self.num1 % self.num2

    def pow(self):
        return self.num1 ** self.num2

    def floordiv(self):
        return self.num1 // self.num2


# create tests for calculator class


# create a calculator object
calc = Calculator(10, 5)

# print the result of each method

print(calc.add())
print(calc.sub())
print(calc.mul())

print(calc.div())
print(calc.mod())
print(calc.pow())

print(calc.floordiv())
