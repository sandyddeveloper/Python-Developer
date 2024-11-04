class Animal:
    def sound(self):
        print("Animal make a sound")
        
class Dog(Animal):
    # pass
    def sound(self):
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Birds Sing")
    


a1 = Animal()
a1.sound()

d1 = Dog()
d1.sound()


b1 = Bird()
b1.sound()
        