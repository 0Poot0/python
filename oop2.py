
class Person:
    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno

    def printOutput(self):
        print("My name is:" ,self.name, "and my rollno is : ", self.rollno)

person1=Person("antara","08")
person2=Person("arpita","09")
person1.printOutput()
person2.printOutput()