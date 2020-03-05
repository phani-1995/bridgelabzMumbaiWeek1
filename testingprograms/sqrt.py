# import math
def sqrt(c,epsilon):
    t=c
    while abs(t - c/t) > epsilon*t:
        t= ((c/t)+t)/2
        return t
epsilon=1 * 10 ** (-15)
c=int(input("Enter a positive integer: "))
if (c<=0):
    print("number cant be negative or zero")
    c = int(input("Enter a positive integer: "))
print("Square root of number is: ", sqrt(c,epsilon))
sqrt(c,epsilon)



################################################################
#
# def sqrt(c, e):
#     # Newtons method
#     t = c
#     while abs(t - c / t) > e:
#         t = (c / t + t) / 2
#     return t
#
#
# if __name__ == '__main__':
#     epsilon = 1 * 10 ** -15
#     positive_int = int(input("Enter a positive number"))
#     # checks weather given num is positive or not
#     if positive_int <= 0:
#         print("Number cant be negitive or zero:")
#         positive_int = int(input("Enter a positive number"))
#
#     print("Squareroot of number is: ", sqrt(positive_int, epsilon))
#

