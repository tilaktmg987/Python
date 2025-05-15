'''
1 for snake
-1 for water
0 for gun
'''
import random

computer= random.choice([1, -1, 0])

user=input("enter you choice(s,w,g): ")
gameDict={"s":1,"w":-1,"g":0}
userchoose=gameDict[user]
reverseDict={1:"snake", -1:"water", 0:"gun" }

print(f"computer choose {reverseDict[computer]} and you choose {reverseDict[userchoose]}")

if(computer==userchoose):
    print("You both draw!")
else:
    if(computer==-1 and userchoose==1): 
        print("You won!")
    elif(computer==-1 and userchoose==0):  
        print("You lose!")
    elif(computer==1 and userchoose==-1):
        print("You lose!")
    elif(computer==1 and userchoose==0): 
        print("You won!")
    elif(computer==0 and userchoose==1): 
        print("You lose!")
    elif(computer==0 and userchoose==-1): 
        print("You won!")
    else:
        print("something went wrong")