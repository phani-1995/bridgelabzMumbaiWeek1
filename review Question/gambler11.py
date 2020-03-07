import random
def gambler(stake,num_of_days):
    bet=1
    win=loss=temp=0
    for j in range(1,num_of_days):
        if (random.random()>0.5):
            win=win+1
            stake=stake+bet
            if stake == stake // 2:
                break
            else:
                loss=loss+1
                stake=stake-bet
            if (stake == 0):
                print("The game completed")
gambler(100,20)







