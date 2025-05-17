# The game() function in a program lets a user play a game and returns the score
# as a n integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever
# the game() function breaks the Hi-score.

def game():
    import random

    score=random.randint(1,100)

    print("playing games....")

    with open("hi-score.txt") as f:
        highest=f.read()
        if(highest==""):
            highest=0
        else:
            highest=int(highest)
    
    print(f"your score is {score}")
    if(score>highest):
        with open("hi-score.txt","w") as f:
            f.write(str(score))


game()