#Normal class 
class Student:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print("My name is",self.name)

s1 = Student("Sagar")
s1.introduce() #introduce is an instance method 
    
#Class Method 
class Student:
    collage = "HRIT University" # clsss Attribute

    def __init__(self,name):
        self.name = name

    @classmethod   # class method
    def show_collage(cls):
        print(cls.collage) # Takes the class itself as its first parameter.

    @classmethod
    def change_collage(cls,name):
        cls.collage = name


Student.show_collage()
Student.change_collage("Delhi University") # changing class attribute 
print(Student.collage)

#Static class
class Student:
    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100

print(Student.is_valid_marks(85))
print(Student.is_valid_marks(150))