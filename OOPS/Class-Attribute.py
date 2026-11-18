class Student:
    collage="HRIT University"  #Class attribute

    def __init__(self,name,age):
        self.name=name
        self.age=age


s1 = Student("Sagar",20)
s2 = Student("Rahul",21)

print(s1.name)
print(s2.name)

print(s1.collage)
print(s2.collage)

#Changing Instance v/s Class Attribute
class Student:
    college="HRIT University"

    def __init__(self,name):
        self.name = name

s1 = Student("Sagar")
s2 = Student("Rahul")

s1.college = "IIT Delhi" #This create an instance attribute

print(s1.college)
print(s2.college)
print(Student.college)

#REAL-WORLD Example
class BankAccount:
    bank_name = "SBI"

    def __init__(self,name,balance):
        self.name = name
        self.balance =balance


account1 = BankAccount("Sagar",5000)
account2 = BankAccount("Rahul",8000)

print(account1.name)
print(account2.balance)
print(account1.bank_name)

print(account2.name)
print(account2.balance)
print(account2.bank_name)