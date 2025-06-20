def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
    print("🌡️ Temperature Conversion Tool 🌡️")
    print("1. Celsius → Fahrenheit & Kelvin")
    print("2. Fahrenheit → Celsius & Kelvin")
    print("3. Kelvin → Celsius & Fahrenheit")
    print("4. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3/4): "))
            
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                kelvin = celsius_to_kelvin(celsius)
                print(f"\n{celsius}°C is equal to:")
                print(f"- {fahrenheit:.2f}°F")
                print(f"- {kelvin:.2f} K")
            
            elif choice == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                kelvin = fahrenheit_to_kelvin(fahrenheit)
                print(f"\n{fahrenheit}°F is equal to:")
                print(f"- {celsius:.2f}°C")
                print(f"- {kelvin:.2f} K")
            
            elif choice == 3:
                kelvin = float(input("Enter temperature in Kelvin: "))
                celsius = kelvin_to_celsius(kelvin)
                fahrenheit = kelvin_to_fahrenheit(kelvin)
                print(f"\n{kelvin} K is equal to:")
                print(f"- {celsius:.2f}°C")
                print(f"- {fahrenheit:.2f}°F")
            
            elif choice == 4:
                print("Exiting... Thanks for using! ❄️🔥")
                break
            
            else:
                print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    temperature_converter()
