n=int(input("Enter a number: "))
rslt=list(map(lambda x: 2 ** n, range(n)))
for i in range(n):
    print("2 raised to power ", i, "is", rslt[i])