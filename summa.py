import sys
import random

print("")
playerchoice = input('Enter..\n1 for Rock,\n2 for Paper,\n3 for Scissores:\n\n')

player = int(playerchoice)

if player <1 or player > 3:
    sys.exit("You Must enter 1, 2, or 3.")
    
computer = random.choice("123")

comp = int(computer)

print("")
print("You choose" + playerchoice + ".")
print("Python choose" + computer + ".")
print("")

if player == comp:
    print("Match Draw..")
elif player == 1 and comp == 2:
    print("You Won the match")
elif player == 2 and comp == 1:
    print("Comp is the winner..")
elif player == 2 and comp == 3:
    print("Comp is the Winner")
elif player == 3 and comp == 2:
    print("You Won the match")
elif player == 3 and comp == 1:
    print("Comp is the winner")
elif player == 1 and comp == 3:
    print("YOu are the winner")
else:
    print("Something went Worng")