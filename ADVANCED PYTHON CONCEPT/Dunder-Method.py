#Dunder/Magic Method :- special method in python whose name start and end with (_ _)
 # 1)__init__ :- Object Initialisation

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Alice",30)
print(p.name,p.age)

# 2) __add__,__sub__,__mul__ :- Operator Overloading
class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)

# 3) __len__ :- Define Behavior for len()
class Book:
    def __init__(self, title, pages):
     self.title = title
     self.pages = pages

    def __len__(self):
        return self.pages

b = Book("Python 101",250)
print(len(b)) #250

# 4)__str__ and __repr__ :-String Representation
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Person({self.name}),({self.age})" #User-friendly

  def __repr__(self):
    return f"Person(name = '{self.name}',age={self.age})" #Unambiguous , for debugging 

p = Person("Alice",30)
print(str(p))
print(repr(p))
print(p)