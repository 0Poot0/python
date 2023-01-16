class Person:
    def __init__(self):
        self.name="Antara"
        self.age=18

    def updateName(self,name):
        self.name=name

    def compareAge(self,other):
        if self.age==other.age:
            return True
        else:
            return False

person1=Person()
person2=Person()

#person1.updateName("ABC")
#person2.name="Atul"
person1.age=22
person2.name="Baishali"

if person1.compareAge(person2):
    print("They are of same age..")
else:
    print("They have different ages...")

print(person1.name,person1.age)
print(person2.name,person2.age)

