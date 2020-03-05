def Money(money):
    notes=[1000,500,100,50,10,5,1]
    note_counter=[0,0,0,0,0,0,0]
    for i in notes:
        for j in note_counter:
            if money>=i:
                j=money//i
                money=money - j*i
                print(i, ":", j)
Money(39876)