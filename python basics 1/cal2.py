import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input for square root"

def power(x, y):
    return x ** y

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice in ('1', '2', '3', '4', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice == '5':
        num1 = float(input("Enter a number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"Square root of {num1} = {square_root(num1)}")
    elif choice == '6':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 7.")
