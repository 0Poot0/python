class student:

    numberOfSubjects=5

    def __init__(self,marks1,marks2,marks3):
        self.web=marks1
        self.python=marks2
        self.math=marks3

    def average(self):
        print("average= ",(self.web+self.python+self.math)/3)

    # def getMarks(self):
    #     return self.math #Accessors

    # def setMarks(self,marks):
    #     self.math=marks #Mutators
    
    
    @classmethod
    def classMethodExample(cls):
        return cls.numberOfSubjects

    @staticmethod
    def staticMethodExample():
        print("This is an example of static method.")

student1=student(5,4,3)
student2=student(7,8,9)
student3=student(1,6,9)

print(student.classMethodExample())
student.staticMethodExample()
#student1.average()

