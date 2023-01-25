class Rect:
    def calculatearea(self,length=None,breadth=None):
        if length!=None and breadth!=None:
            return length*breadth
        elif length!=None:
            return length*length


rectangle=Rect()
print(rectangle.calculatearea(2,3))
print(rectangle.calculatearea(2))
