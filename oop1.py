a=5
print(type(a))

class Laptop:
    def __init__(self,name,processor):
        self.name="Asus"
        self.processor="i9"
    

    def printOutput(self):
        print("My laptop name is :" ,self.name, "and the processor is : ", self.processor)

laptop1=Laptop("antara","i9")
laptop2=Laptop("arpita","i7")
# print(id(laptop1))
# print(id(laptop2))
laptop1.printOutput()

#laptop1.config()
#laptop2.config()