class Animal:
    def __init__(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


a1 = Animal()
d1 = Dog()

a1.sound()
d1.sound()