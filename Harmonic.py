def Harmonic(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum+1/i
    print(sum)
n=int(input("Enter the number:"))
Harmonic(n)
