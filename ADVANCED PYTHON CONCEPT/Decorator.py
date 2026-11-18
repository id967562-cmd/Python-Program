#Normal function 
def greet():
    print("Hello , Sagar!")

greet()

#Creating first Decorator
def my_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")

    return wrapper

@my_decorator # greet = my_decorator(greet)
def greet():
    print("Hello , Sagar!")

#greet function is passed to my_decorator
#The returned Wrapper function is  assigned to name greet()

greet()  # greet() = wrapper()