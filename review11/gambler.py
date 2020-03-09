import random
def gambler(stake,num_of_times):
    bet=1
    win=loss=temp=0
    for i in range(1, num_of_times):
        if (random.random() >= 0.5):
            win = win + 1
            stake = stake + bet
        if (stake == goal):
            break
        else:
            loss = loss + 1
            stake = stake - bet

        if (stake == stake // 2):
            break
            print("The game was completed for the day")
stake = int(input("Enter the amount: "))
num_of_times=int(input("Enter the number of times you want to play: "))
gambler(stake,num_of_times)