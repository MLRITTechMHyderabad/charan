import random
li1=[1,2,3,4,5,6]
li2=[1,2,3,4,5,6]
round=int(input("enter how many numbers you want to play"))
dic={"player_1":0,"player_2":0}
inc=1
def player_1():
    a=random.randint(1,6)
    b=random.randint(1,6)
    sum=a+b
    count=0
    for i in li1:
        for j in li2:
            if sum==i+j:
                count=count+1
    prob=float(count/36)*100
    return prob
def player_2():
    a=random.randint(1,6)
    b=random.randint(1,6)
    sum=a+b
    count=0
    for i in li1:
        for j in li2:
            if sum==i+j:
                count=count+1
    prob=float(count/36)*100
    return prob
def win(player_1,player_2,inc):
    if(player_1>player_2):
        dic["player_1"]+=1
        print("player 1 is the winner in ",inc)
    elif (player_2>player_1):
        dic["player_2"]+=1
        print("player 2 is the winner in ",inc)
    else:
        print("it is tie match in ",inc)
while(round>0):
    p1=player_1()
    p2=player_2()
    win(p1,p2,inc)
    inc+=1
    round=round-1
def declare(dic):
    if dic["player_1"]>dic["player_2"]:
        print("player 1 is the winner")
    elif dic["player_2"]>dic["player_1"]:
        print("player 2 is the winner")
    else:
        print("TIE")
declare(dic)