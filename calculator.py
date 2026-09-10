import sys
def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    operation = sys.argv[3]
    if operation == "add":
        result = add_numbers(num1, num2)
        operation_name = "Addition"
    elif operation == "subtract":
        result = subtract_numbers(num1, num2)
        operation_name = "Subtraction"
    elif operation == "multiply":
        result = multiply_numbers(num1, num2)
        operation_name = "Multiplication"
    elif operation == "divide":
        result = divide_numbers(num1, num2)
        operation_name = "Division"
    else:
        result = "Invalid operation"
        operation_name = "Invalid Operation"
    print("=================================")
    print("Calculator Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Operation    : {operation_name}")
    print(f"Result       : {result}")
    print("=================================")