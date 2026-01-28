while True:
    print("\nTemperature Conversion Menu")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"Temperature in Celsius: {c:.2f}°C")
    elif choice == 2:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"Temperature in Fahrenheit: {f:.2f}°F")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Try again.")