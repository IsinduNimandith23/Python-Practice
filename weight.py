unit = input("Enter which unit: kg or pound: ")
weight = float(input(f"enter weight: "))

if unit == "kg" :
    result = weight * 2.205
    print(result)
elif unit == "pound":
    result = weight / 2.205
    print(result)
else:
    print("Please choose a weight")


