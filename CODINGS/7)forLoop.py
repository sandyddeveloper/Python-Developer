for i in range(1,6):# this is row
    if i in [1, 5]:
        for j in range(1,4):
            if j in [1,2,3]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
        
    elif i== 2:
        for j in range(1,4):
            if j in [2]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    elif i ==3:
        for j in range(1,4):
            if j in [2]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    else :
        for j in range(1,4):
            if j in [2]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    
    
for i in range (1,6):
    if i in [1, 5]:
        for j in range(1, 6):
            if j in [1,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    elif i == 2 :
        for j in range(1, 6):
            if j in [2,4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    elif i == 4 :
        for j in range(1, 6):
            if j in [2,4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    else:
        for j in range(1,6):
            if j in [3]:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()
        
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1 or i == 4 or i == 7) and (1 <= j <= 5):
            print("*", end=" ")
        elif (i == 2 or i == 3) and j == 1:
            print("*", end=" ")
        elif (i == 5 or i == 6) and j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range (1,6):
    for j in range(1,6):
        if (i == 1 or i == 3 or i == 5):
            print("*", end=" ")
        elif (i == 2 or i == 4 ) and j == 1:
            print("*" , end=" ")
        else:
            print(" ", end= " ")
    print()


for i in range(1,6):
    for j in range(1,6):
        if( i == 1 or i == 5):
            print("*", end=" ")
        elif (i==2) and j ==4:
            print("*", end=" ")
        elif (i==3) and j == 3:
            print("*", end=" ")
        elif (i==4) and j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
        
        
for i in range(1,6):
    for j in range(1,6):
        if (i == 1 or i == 3 or i == 5) and j in (1,2,3,5):
            print("*", end=" ")
        elif (i == 2 or i == 4) and j in (3,5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
            
            