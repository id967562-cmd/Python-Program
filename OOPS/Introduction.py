class Student:             # Here Student is Blueprint - from that blue print i         
    def study(self):       # can easily call other students marks , subject class etc 
        print("Student is studying")

s1 = Student()  #Here s1 is object
s1.study()

#Second Example
class Students:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def introduce(self):
        print("Name:",self.name)
        print("Age:",self.age)

s2=Students("Sagar",20)
s3=Students("Rahul",21)

s2.introduce()
print()
s3.introduce()

#Third Example
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1=student("Sagar",20)
s1.introduce()
