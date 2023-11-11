
#CHIKOMBE CANON ALLAN
#SCT211-0019/2020


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    else:
        try:
            print(f"{num1} + {num2} = {add(num1, num2)}")
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except Exception as e:
            print("An error occurred:", e)
