def add(x, y):
    z = x + y
    print('Sum is:', z)

def subtract(x, y):
    z = x - y
    print('Subtract is:', z)

def multiply(x, y):
    z = x * y
    print('Multiplication is:', z)

def divide(x, y):
    if y == 0:
        print("Error!")
    else:
        z = x / y
        print('Division is:', z)

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice from 1 to 5: ")
    if choice == '5':
        print("Exit")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            add(num1, num2)
        elif choice == '2':
            subtract(num1, num2)
        elif choice == '3':
            multiply(num1, num2)
        elif choice == '4':
            divide(num1, num2)
    else:
        print("Invalid input")
