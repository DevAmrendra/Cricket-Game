import random
import time
import os
from commentary import commentary_dict

def play(player, target):
    
    val=[0,1,2,3,4,6,"Wide","No_ball",'Out']
    score=0
    initial=0
    loop=12
    ball=0
    arr=[]
         
    print(f"Team {player} current runs: {score} in {ball} balls")

    while initial<loop :
        x=random.choice(val)
        arr.append(x)
        
        if(x=='Out'):
            print(random.choice(commentary_dict['out']))
            time.sleep(2)
            os.system('cls')
            break
        elif(x=='Wide'):
            loop+=1
            score+=1
            print(random.choice(commentary_dict['wide']))
            time.sleep(2)
            os.system('cls')
        elif(x=='No_ball'):
            score+=1
            loop+=1
            print(random.choice(commentary_dict['no_ball']))
            time.sleep(2)
            os.system('cls')
        else:
            
            match x:
                case 0:
                    print(random.choice(commentary_dict[0]))
                case 1:
                    print(random.choice(commentary_dict[1]))
                case 2:
                    print(random.choice(commentary_dict[2]))
                case 3:
                    print(random.choice(commentary_dict[3]))
                case 4:
                    print(random.choice(commentary_dict[4]))
                case 6:
                    print(random.choice(commentary_dict[6]))


            time.sleep(2)
            os.system('cls')
            score=score+x
            ball+=1
        initial+=1
        
        print(f"Team {player} current runs: {score} in {ball} balls")
        if (target != 0):
            print(f"Team {player} need {target-score} runs to win in {12-ball} balls ")
            if (score >= target):
                os.system('cls')
                break
        time.sleep(2)
        
        
    return score

firstPlayer = input("Player 1: ")
secondPlayer = input("Player 2: ")
target=0

time.sleep(2)
os.system('cls')
team_1=play(firstPlayer, target)
print(f"{firstPlayer} scored {team_1} runs")

target = team_1+1

print("Second innings is going to start...")
time.sleep(3)

team_2=play(secondPlayer, target)
print(f"{secondPlayer} scored {team_2} runs")

print("Final result")
time.sleep(2)


if(team_1>team_2):
    print(f"{firstPlayer} win")
elif (team_1==team_2):
    print("Tie")
else:
    print(f"{secondPlayer} win")

