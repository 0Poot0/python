class bird:
   def category(self):
    print("This is a category of bird")

   def fly(self):
    print("I can fly")

class crow(bird):
    pass
class sparrow(bird):
    def sizeParameter(self):
        print("I am small in size.")
class ostrich(bird):
    def fly(self):
        print("I cannot fly.")


objsparrow=sparrow()
objcrow=crow()
objostrich=ostrich()
objbird=bird()

objbird.category()
objcrow.category()
objcrow.fly()
objsparrow.category()
objsparrow.fly()
objostrich.category()
objostrich.fly()


