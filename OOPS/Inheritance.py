#Inheritance initializers
class Student:                      #Parent Class
    def __init__(self,name,age):    
        self.name=name
        self.age=age

    def introduce(self):
      print("Name:",self.name)
      print("Age:",self.age)

class EngineeringStudent(Student):  #Child class
    pass

class MedicalStudent(Student):     #Child class
    pass


s1 = EngineeringStudent("Sagar", 21)
s2 = MedicalStudent("Rohit",22)
s1.introduce()
s2.introduce()

#super()---> use to access methods from a parent class,
            # commonly to call the parent's initializer from a child class

class Student:

    def __init__(self,name,favbook):
        self.name = name
        self.favbook = favbook

class EngineeringStudent(Student):

    def __init__(self,name,favbook,branch):
        super().__init__(name,favbook)
        self.branch = branch

s1 = EngineeringStudent("Sagar","Atomic-Habit","CSE")

print(s1.name)
print(s1.favbook)
print(s1.branch)


