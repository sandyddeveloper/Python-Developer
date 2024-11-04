# # class Company():
# #     def __init__(self):
# #         self.companyName = "Google"
    
# #     def companyName (self):
# #         print(self.companyName)
        
# # c1 = Company()
# # c1.companyName()

# # #Public
# # class car():
# #     def open_door_and_proceed(self):
# #         print("Door Opened")
# #         print("Enter into car & started")
        
# # my_car = car()
# # my_car.open_door_and_proceed()

# #Protected
# class car():
#     def open_door_and_proceed(self):
#         print("Door Opened")
#         print("Enter into car & started")
#         self._accelerate()
        
#     def _accelerate(self):#protected(_)
#         print("Throttle incresed")
        
# my_car = car()
# my_car.open_door_and_proceed()

# #Private
# class car():
#     def open_door_and_proceed(self):
#         print("Door Opened")
#         print("Enter into car & started")
#         self._accelerate()
        
#     def _accelerate(self):#protected(_)
#         print("Throttle incresed")
#         self.__engine_performing()
        
#     def __engine_performing(self):#Private
#         print("Performating Well..")
        
# my_car = car()
# my_car.open_door_and_proceed()


class encapsulation:
    def __init__(self,accountholder,balance=0):
        self._accountholder=accountholder #it is a protected variable
        self.__balance=balance #it is a private variable
    def getbalance(self):
        return self.__balance
    def amountdeposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited ${amount},newbalance=${self.__balance}")
        else:
            print(f"amount cannot be negative")

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw ${amount},newbalance=${self.__balance}")
        else:
            print("insufficient fund")

    def setaccountholder(self,new_accountholder):
        if new_accountholder:
            self._accountholder=new_accountholder
            print(f"accountholder changed to {self._accountholder}")
        else:
            print("invaliad accountholder name")

    def getaccountholder(self):
        return self._accountholder

account=encapsulation('abc',70000)
a=account.getaccountholder()
print(a)
print(account.getbalance())
account.amountdeposit(500)
print(account.getbalance())
account.withdraw(100)
account.withdraw(1000)
print(account.getbalance())
account.withdraw(69000)
print(account.getbalance())
print("-----------------------")
account._accountholder='suresh'
o=account.getaccountholder()
print(o)
account.setaccountholder('VIP')
a=account.getaccountholder()
print(a)