def pal(a,b):
    a += 1
    for i in range(a, b):
        y = True
        if (str(i) == str(i)[::-1]):
            if (i > 2):
                for a in range(2, i):
                    if (i % a == 0):
                        y = False
                        break
                if y:
                    print(i)
pal(0,1000)

