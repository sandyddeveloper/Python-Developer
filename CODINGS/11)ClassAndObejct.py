# class human:
#     def breath():
#         pass
#     def eat():
#         pass
#     def sleep():
#         pass


# class Employee:
#     company = 'Tutorial Gateway'

#     def __init__(self, name, age, gender):
#         print('hi')
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def func_message(self):
#         print('Welcome to Programming')

#     def printmsg(self):
#         print(f"{self.name},welcome to oops class and is age was={self.age} and gender was={self.gender}")


# emp1 = Employee('Jack', 25, 'Male')
# emp2 = Employee('Rose', 23, 'FeMale')

# print(emp1.company)
# emp1.func_message()
# print(emp1.name)
# print(emp1.age)
# print(emp1.gender)
# emp1.printmsg()
# emp2.printmsg()
# emp2.age=20
# emp2.printmsg()

class cal():
    def add(self, a, b):
        self.addition = a+b
        print(self.addition)
    def sub(self, a, b):
        self.subt = a-b
        print(self.subt)
    def mul(self, a, b):
        self.mult = a *b
        print(self.mult)
    def div(self, a, b):
        self.divd = a/b
        print(self.divd)
        
summa = cal()

summa.add(12, 5)

