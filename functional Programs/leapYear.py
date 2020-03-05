def Leap_year():
    if (y%4 == 0) or (y%100 == 0):
        print("The year is a leap year")
    else:
        print("The year is not leap year")
y=int(input("Enter the year:"))
Leap_year()