class Student: #Created class of Student

    def __init__(self,name,age): #Constructor called__INIT__ 
        self.name=name            #self refers to the current object.
        self.age=age              #self---->s1

    def introduction(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1 = Student("Sagar",20)
s1.introduction()