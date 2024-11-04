# One
# class Shape():
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def area(self):
#         l = int(input())
#         b = int(input())
#         return l * b
    
# obj = Rectangle()
# print(obj.area())

# Two
    # class person():
    #     def __init__(self, name):
    #         self.name = name
            
    # class Student(person):
    #     def __init__(self,name, grade):
    #         self.grade = grade
    #         super().__init__(name)
            
    #     def display(self):
    #         print(self.name, self.grade)
            
    # a1=Student("Sandy","A")
    # a1.display()
    
    
#Four
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department= department
    
    def display(self):
        print(self.name, self.salary, self.department)
        
obj = Manager("SANDY", "50000", "PYTHON DEV")
obj.display()

        

    

        