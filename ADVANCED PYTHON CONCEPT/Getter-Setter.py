# Traditional Approch
class Person:
    def __init__(self,name):
        self._name=name # Convention underscore(_) denotes a private attribute.

    def get_name(self):
        return self._name

    def set_name(self,new_name):
        self._name = new_name

p= Person("Alice")
print(p.get_name()) #Alice

p.set_name("Bob")
print(p.get_name()) #Bob
        




class Student:
    def __init__(self,marks):
        self.__marks = marks # Pyhon name mangling
     # Name Mangling --> Mechanism that changes the name of an attribute
     #                  beginning with two underscores(__)inside a class.
     # Prevent accidental access / modification of class attributes form outside of class.

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks!")

    @marks.deleter  # Delete a property 
    def marks(self):
        del self.__marks

s = Student(80)

print(s.marks)
del s.marks
# print(s.marks)  Attribute-Error: "marks" object has no attribute '_name'


# s.marks = 95
# print(s.marks)

# s.marks = 150 

