def Windchill():
    # checks the condition weather it is in range or not
    if t > 50 or v > 120 or v < 3:
        print("Formula not valid for this conditions pls enter t<50 and v between 3 and 120")
        return WindChill()
    else:
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
        print("Windchill:", w)
t=float(input("Enter the temperature less than 50F: "))
v=float(input("Enter the velocity between 3 and 120: "))

Windchill()
