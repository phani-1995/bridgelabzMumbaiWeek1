import random
n=int(input("Enter the number: "))
Heads=0
Tails=0
for i in range(n):
    flip=random.randint(0,1)
    if flip>=0.5:
        Heads=Heads+1
    else:
        Tails=Tails+1
print("Heads count:",Heads)
print("Tails Count: ",Tails)
