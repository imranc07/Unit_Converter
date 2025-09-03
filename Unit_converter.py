# Problem Statement:
# Create a CLI app that converts units (like km to miles, celsius to Fahrenheit) based on user input.

# Conversion function: Kilometers to Miles
def km_to_miles(km):
    return km * 0.621371

# Conversion function: Miles to Kilometers
def miles_to_km(miles):
    return miles / 0.621371

# Conversion function: Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9 / 5) + 32

# Conversion function: Fahrenheit to Celsius
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Display menu for the user
print("🌍 Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

# Get user's choice
choice = input("Choose conversion (1-4): ")

try:
    # Kilometers to Miles
    if choice == '1':
        km = float(input("Enter Kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")

    # Miles to Kilometers
    elif choice == '2':
        miles = float(input("Enter Miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")

    # Celsius to Fahrenheit
    elif choice == '3':
        c = float(input("Enter Celsius: "))
        print(f"{c} ℃ = {c_to_f(c):.2f} ℉")

    # Fahrenheit to Celsius
    elif choice == '4':
        f = float(input("Enter Fahrenheit: "))
        print(f"{f} ℉ = {f_to_c(f):.2f} ℃")

    # Invalid menu option
    else:
        print("❌ Invalid choice")

# Handle invalid numeric input
except ValueError:
    print("❌ Please enter a valid number")
