class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def getName(self):
        return self.__name

    def getAge(self):   # getter method(accessor)
        return self.__age


person1=Person("Antara",19)
print(person1._Person__name)
