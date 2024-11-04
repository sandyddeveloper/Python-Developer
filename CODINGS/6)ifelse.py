# rcb = "lose"
# if(rcb == "win"): # in this part , thr codition will execute , if its true then if parts take place or else part will take place
#     print("Eesala cup Namde")# trun condition
# else: # false condition
#     print("Eesala cupu lollipopu")


import random

player = input("ente the object: ")
comp = random.choice(["ROCK", "PAPER", "SCS"]) 

if player == "ROCK" and comp == "PAPER":
    print("Comp is wonner")
elif player == "PAPER" and comp == "ROCK":
    print("YOur the winner")
elif player == "ROCK" and comp =="SCS":
    print("knkdvn")
else:
    print("try again")


