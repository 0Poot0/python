class Person:
    def __init__(self):
        self.name="Antara"
        self.age=18

    def updateName(self,name):
        self.name=name

person1=Person()
person2=Person()

person1.updateName("ABC")
#person2.name="Atul"

print(person1.name)
print(person2.name)



