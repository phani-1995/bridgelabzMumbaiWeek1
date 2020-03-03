import math
def Distance(x,y):
    pt1=(x,y)
    pt2=(0,0)
    result = math.sqrt(x*x + y*y)
    print("The Euclidean distance is: ",result)
x=float(input("Enter a x value: "))
y=float(input("Enter a y value: "))
Distance(x,y)