Valid_Operations = ["add", "subtract", "multiply", "divide"]
operation = input("What operation would you like to perform? (add, subtract, multiply, divide): ")

if operation not in Valid_Operations:
        print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
else:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    if operation == "add":
        result = x + y
        print(f"The result of adding {x} and {y} is: {result}")
    elif operation == "subtract":
        result = x - y
        print(f"The result of subtracting {y} from {x} is: {result}")
    elif operation == "multiply":
        result = x * y
        print(f"The result of multiplying {x} and {y} is: {result}")
    elif operation == "divide":
        if y != 0:
            result = x / y
            print(f"The result of dividing {x} by {y} is: {result}")
        else:
            print("Error: Division by zero is not allowed.") 