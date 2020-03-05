##Ckecking for palindrome
def prime_pali(a,b):
# a = 0
# b = 1000
    a += 1
    for i in range(a,b):
            y = True
            if(str(i) == str(i)[::-1]):
                if(i>2):
                    for a in range(2,i):
                        if(i%a==0):
                            y = False
                            break
                    if y == True:
                        print(i)
prime_pali(0,1000)
#Ckecking for anagram
def prime_ana(c,d):
    a += 1
    for j in range(c,d+1):
        for k in range(1,d+1):
            z=True
            x1=sorted(str(j))
            x2=sorted(str(k))
            if (x1 == x2):
                if (j>2) and (k>2):
                    for c in range(2,j):
                        for ana in range(2,k):
                            if (j%c==0):
                                y=False
                                break
                    if (y==True):
                        print(j)
prime_ana(0,1000)






