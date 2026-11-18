# Function within function
def f1():
    s='I love GeeksforGeeks'
    def f2():
        r="I am sagar"
        print(r)
        print(s)

    f2()
f1()

# Return Statement
def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-5))

# Pass-by-value & Pass-by-Reference
def myfun1(x): #--->Pass-By-Reference
    x[0]=20

b=[10,50,30,12]
myfun1(b)
print(b)

def myfun2(x):  #===>Pass-By-value
    x=3

a=19
myfun2(a)
print(a)