print("Temperature Converter")
Temp_1 = input("Enter the temperature scale you want to convert from (C for Celsius, F for Fahrenheit, K for Kelvin): ")

while Temp_1 not in ["C", "F", "K"]:
    Temp_1 = input(f"Invalid temperature scale, '{Temp_1}'. Please enter a valid temperature scale (C, F, K): ")
Temp_2 = input("Enter the temperature scale you want to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ")

while Temp_2 not in ["C", "F", "K"]:
    Temp_2 = input(f"Invalid temperature scale, '{Temp_2}'. Please enter a valid temperature scale (C, F, K): ")

while Temp_1 == Temp_2 or Temp_1 not in ["C", "F", "K"] or Temp_2 not in ["C", "F", "K"]:
    Temp_1 = input(f"Same/ivalid temperature scale, '{Temp_1}'. Please enter a different temperature scale (C, F, K): ")
    Temp_2 = input("Enter the temperature scale you want to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ")

else:
    Value = float(input("Enter the temperature value you want to convert: "))

    if Temp_1 == "C" and Temp_2 == "F":
        F = (Value * 9/5) + 32
        print(f"{Value} degrees Celsius is equal to {F} degrees Fahrenheit.")
    elif Temp_1 == "C" and Temp_2 =="K":
        K = Value + 273.15
        print(f"{Value} degrees Celsius is equal to {K} Kelvin.")
    elif Temp_1 == "F" and Temp_2 == "C":
        C = (Value-32) * 5/9
        print(f"{Value} degrees Fahrenheit is equal to {C} degrees Celsius.")
    elif Temp_1 == "F" and Temp_2 == "K":
        K = (Value-32) * 5/9 + 273.15
        print(f"{Value} degrees Fahrenheit is equal to {K} Kelvin.")
    elif Temp_1 == "K" and Temp_2 == "C":
        C = Value - 273.15
        print(f"{Value} Kelvin is equal to {C} degrees Celsius.")
    elif Temp_1 == "K" and Temp_2 == "F":
        F = (Value - 273.15) * 9/5 + 32
        print(f"{Value} Kelvin is equal to {F} degrees Fahrenheit.")