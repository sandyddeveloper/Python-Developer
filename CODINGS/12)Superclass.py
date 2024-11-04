class a():
    def __init__(self):
        print("A")
    
    def display():
        print("this is A")
        
class b():
    def __init__(self):
        super().__init__()
        print("B")
    
    def display():
        print("this is B")
        
class c(b, a):
    def __init__(self):
        super().__init__()
        print("C")
    
    def display():
        print("this is C")
        
obj = c()


class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()