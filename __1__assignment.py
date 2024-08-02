def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)

while True:
    print("\nSelect operation:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Enter your choice from 1 to 3: ")

    if choice == '3':
        print("Exiting the program.")
        break

    if choice in ['1', '2']:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            celsius_to_fahrenheit(celsius)
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            fahrenheit_to_celsius(fahrenheit)
    else:
        print("Invalid choice.")
