N=int(input("Enter the maximum range: "))
for prime in range(2,N):
    count=0
    for j in range(2,prime//2):
        if(prime%j==0):
            count+=1
    if(count==0):
        print(prime, end=" " )