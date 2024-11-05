name = input("Hey type your Name Mate:")

print("Hey,",name, "Welcome to Play My game Mate ")

can_we_play = input("Do you want to a game Now?").lower()

if can_we_play == "y" or can_we_play =="yes":
    print("Okay wr are going to play this game mate..")
    
    direction = input("Do you want to go left or right Mate?:").lower()
    if direction == "left":
        print("You went left and fell of a cliff, and you die .. Game over mate..")
    elif direction == "right":
        choice = input("Okay, you now see  bridge , do you want to swim user the it or cross it?:").lower()
        if choice == "swim":
            print("You got eaten by an alligator, you die ,, the end mate!")
        elif choice == "cross":
            print("You found the gold and won this game ")
        else:
            print("this reply  is in valid")
    else:
        print("Sorry not a valid reply, you die")
else:
    print("Its okay mate can we play some another time ...")
    
    