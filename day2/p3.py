import random
d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
li=[]
for i in d1:
    for j in d2:
        li.append((i,j))
print(li)
di={}
di1={}
for i in range(2,13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
            c=c+1
    di[str(i)]=c
    prob=float(c/36)*100
    di1[str(i)]=prob
print(di)
print(di1)
def player_1(P1_d1,P1_d2):
    return P1_d1+P1_d2
def player_2(P2_d1,P2_d2):
    return P2_d1+P2_d2
def determine_winner(R,rounds):
    player1_wins=0
    player2_wins=0
    for round in rounds:
        P1_d1,P1_d2,P2_d1,P2_d2=round
        P1_sum=player_1(P1_d1,P1_d2)
        P2_sum=player_2(P2_d1,P2_d2)

        if di1[str(P1_sum)]<di1[str(P2_sum)]:
            player1_wins +=1
        elif di1[str(P2_sum)]<di1[str(P1_sum)]:
            player2_wins +=1
    if player1_wins>player2_wins:
        print("Player 1 wins")
    elif player2_wins>player1_wins:
        print("player 2 wins")
    else:
        print("its a draw match")
R = int(input())
rounds = [tuple(map(int, input().split())) for _ in range(R)]
determine_winner(R,rounds)