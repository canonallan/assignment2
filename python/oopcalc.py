
#SCT211-0019/2020
#CHIKOMBE CANON ALLAN
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        return self.num1 / self.num2

# Usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

calc = Calculator(num1, num2)

print(f"{num1} + {num2} = {calc.add()}")
print(f"{num1} - {num2} = {calc.subtract()}")
print(f"{num1} * {num2} = {calc.multiply()}")
print(f"{num1} / {num2} = {calc.divide()}")
