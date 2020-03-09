import random
def gambler(stake,num_of_times):
    bet=1
    win=loss=temp=0
    for i in range(1, num_of_times):
        if (random.random() >= 0.5):
            win = win + 1
            stake = stake + bet

        else:
            loss = loss + 1
            stake = stake - bet
stake = int(input("Enter the amount: "))
gambler(stake,num_of_times)