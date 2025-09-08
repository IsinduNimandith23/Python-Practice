unit = input("Enter which unit: C for Celcius or F for Farenheit: ")
temperature = float(input(f"Enter temperature: "))

if unit == "C" :
    result = (temperature * 1.8) + 32
    print(result)
elif unit == "F":
    result = (temperature - 32) / 1.8
    print(result)
else:
    print("Please choose a weight")