import random
def gambler(stake,goal,num_of_times,days):
    bet=1
    win=loss= temp=0
    for i in range(1, num_of_times):
        for j in range(1,days):
            if (random.random() >= 0.5):  # if generated random is gt 0.5 gamer wins then stake incremnts by 1  and bets again
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

            temp = i

            if (temp <= days) and (stake == goal):
                print("The goal has reached")
            if (temp == days) and (stake != goal):
                print("Timeup.... Goal not reached")
            else:
                print("No more stake")

            print("No.of Wins:", win)
            print("No.of Loss:", loss)

            if win > loss:
                print("Luckyday:", win)
            else:
                print("Umlucky day: ", loss)

stake = int(input("Enter the amount: "))
goal = int(input("Enter the amount he want to gain: "))
num_of_times=int(input("Enter the number of times you want to play: "))
days=int(input("Enter the number of days: "))
gambler(stake,goal,num_of_times,days)