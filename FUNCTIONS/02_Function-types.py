# 1) Deafult argument
def myfun(x,y=14):
     print("x:",x)
     print("y:",y)

myfun(10)

#Keyword argument
def student(fname,lname):
     print(fname,lname)

student(fname="Sagar",lname='singh')
student(lname="singh",fname='Aman')     

#Positional Argumnet
def nameAge(name,age):
     print("Hi,I am ",name)
     print("My age is ",age)

print("Case-1:")
nameAge("olivia",27)
print("Case-2:")
nameAge(24,"Aman")     

#Aribitrary Argument
def add(*args):
      Total=0
      for num in args: 
        Total+=num
      print("Total:",Total)

add(1,2,3,4,5)

def display(**kwargs):
     for key,value in kwargs.items():
          print(f"{key}:{value}")

display(name="Alice",age=23,city="London")
display(name="Alice",age=54,city="U.S")