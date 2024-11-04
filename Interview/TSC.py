def tcs():
    # n = int(input("Enter the number:"))
    # for i in range(1, n ):
    #     print("*" * i)
    #     n +=1
        
        
        
    # m = int(input("Enter the number:"))
    # for i in range(1, m - 1):
    #     print(str(i) * i)
    #     m = m - 1
        
    # a = int(input())
    # for i in range( a , 0, -1):
    #     print(str(i) * i)
        
        
        
    # n = int(input())    
    # for i in range(1, n +1):
    #     for j in range(1, i + 1):
    #         print(j, end=" ")
    #     print()
    
    
    n = int(input())
    for i in range(1 ,n + 1):
        for j in range(1, i):
            for j in range(i-1, 0, -1 ):
                print(j, end=" ")
            print()
        
        
        
        
   
        
tcs()


