class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Sagar",20)   #Each object has its own seperate value
s2=Student("Rahul",21)   #s1,s2-->different object

print(s1.name)
print(s2.name)

print(s1.age)
print(s2.age)