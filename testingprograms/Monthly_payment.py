def monthly_payment(P, Y, R):
    n = 12 * Y  # years to months
    rate = R / (12 * 100)
    payment = (P * rate) / (1 - ((1 + rate) ** (-n)))

    print(payment)

P = int(input("Enter the principal loan amount: "))
R= int(input("Enter the rate of intrest: "))
Y = int(input("Enter the time period in years: "))
monthly_payment(P, Y, R)

