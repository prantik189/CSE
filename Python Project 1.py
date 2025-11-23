# coverting km to miles
def km_to_miles(km):
    return km * 0.621371

#coverting miles to km
def miles_to_km(miles):
    return miles / 0.621371

# converting celsius to farenheit
def c_to_f(c):
    return (c * 9/5) + 32

# converting farenheit to celsius
def f_to_c(f):
    return (f - 32) * 5/9

# coverting kg to lbs
def kg_to_lbs(kg):
    return kg * 2.20462

# coverting lbs to kg
def lbs_to_kg(lbs):
    return lbs / 2.20462


while True:
    print("\n----- Unit Converter -----")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = float(input("Enter kilometers: "))
        print("Miles:", km_to_miles(value))

    elif choice == "2":
        value = float(input("Enter miles: "))
        print("Kilometers:", miles_to_km(value))

    elif choice == "3":
        value = float(input("Enter Celsius: "))
        print("Fahrenheit:", c_to_f(value))

    elif choice == "4":
        value = float(input("Enter Fahrenheit: "))
        print("Celsius:", f_to_c(value))

    elif choice == "5":
        value = float(input("Enter kilograms: "))
        print("Pounds:", kg_to_lbs(value))

    elif choice == "6":
        value = float(input("Enter pounds: "))
        print("Kilograms:", lbs_to_kg(value))

    elif choice == "7":
        print("Thank you for using Unit Converter!")
        break

    else:
        print("Invalid choice, try again!")