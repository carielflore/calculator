import math


class Calculator:
    def __init__(self):
        self.current_value = ""
        self.result = 0
        self.operation = None
        self.new_number = True

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Modulo by zero")
        return a % b

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def power(self, a, b):
        return a**b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Square root of negative number")
        return math.sqrt(a)

    def floor(self, a):
        return math.floor(a)

    def ceil(self, a):
        return math.ceil(a)
