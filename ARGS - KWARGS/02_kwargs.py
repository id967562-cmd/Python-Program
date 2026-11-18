def student(**kwargs):
    print(kwargs)

student(name ="Sagar", age= 21,city="Ghaziabad")

#Combination of both *args and **kwargs
def demo(*args,**kwargs):
    print("Positional:",args)
    print("Keyword:",kwargs)

demo(10,20,30, name="Sagar",age=21)