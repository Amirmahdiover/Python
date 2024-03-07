Weight = float(input("Weight = "))
Conversion = input("(K)g or (L)bs = ")

if Conversion.upper() == "K":
    Lbs = (Weight * 2.20462).__round__()
    print("Weight in Lbs = " + str(Lbs))
elif Conversion.upper() == "L":
    Kg = (Weight / 2.20462)
    print("Weight in kg = " + str(Kg))
else:
    print("Wrong unit of measurement")

