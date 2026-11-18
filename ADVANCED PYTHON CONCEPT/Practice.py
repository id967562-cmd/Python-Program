def demo(func):
    def wrapper():
        print("A")
        func()
        print("B")

    return wrapper

@demo
def test():
    print("C")

test()

#Output : A--> C --> B