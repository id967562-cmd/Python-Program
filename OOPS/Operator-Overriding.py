a=10
b=20
print(a + b)

a="Hello "
b="Sagar"
print(a+b)

#Same operator(+)-->perform different behaviour

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

n1=Number(10)
n2=Number(20)

print(n1+n2)

# One class with multiple operators
class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return Number(self.value + other.value)
     #  'other' refers to the object on the *right* side of the +

    def __sub__(self,other):
        return Number(self.value - other.value)
    def __mul__(self,other):
        return Number(self.value * other.value)
    def __eq__(self,other):      #Overloading == operator
        return self.value == other.value




a=Number(20)
b=Number(10)


print((a + b).value) #a__add__(b)
print((a-b).value)
print((a*b).value)
print(a==b)