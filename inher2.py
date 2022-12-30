class A:
    def __init__(self):
        print("This is init of method A")

    def method1(self):
        print("This is method 1")


class B(A):
    def __init__(self):
        super().__init__()
        print("This is init of method B")

    def method2(self):
        print("This is method 2")


objB=B()