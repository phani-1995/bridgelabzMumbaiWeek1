def binary_search(a,f,l):
    # first=0
    # last=N-1
    found=False
    while f<=l and not found:
        middle=(l+f)//2
        print(a[middle],"Is your number?")
        if input() == "Y":
            print()
            return a[middle]
        elif input("Is num greater than your num?")== "Y":
            l=middle-1
            return l
        else:
            f=middle+1
        return found

a=[i for i in range(int(input("Enter a range: ")) + 1)]
print("Guess a number: ")
f=0
l=len(a)-1
k=binary_search(a,f,l)
if k:
    print(k,"Found")
else:
    print("Your number is out of range")

